import numpy
import numpy as np
import cv2
import os

BLUR_RADIUS = 3
MORPH_KERNEL_SIZE = (11,11)
DEFAULT_ARC_LENGTH = 0.09
EDGE_LIMIT = 800




def intersect(aa,bb,cc,dd):
    def determinant(v1, v2, v3, v4):
        return v1 * v4 - v2 * v3
    delta = determinant(bb[0] - aa[0], cc[0] - dd[0], bb[1] - aa[1], cc[1] - dd[1])
    if delta <= (1e-6) and delta >= -(1e-6):
        return False

    namenda = determinant(cc[0] - aa[0], cc[0] - dd[0], cc[1] - aa[1], cc[1] - dd[1])
    if namenda > 1 or namenda < 0:
        return False
    miu = determinant(bb[0] - aa[0], cc[0] - aa[0], bb[1] - aa[1], cc[1] - aa[1]) / delta
    if miu > 1 or miu < 0:
        return False
    return True


def check_convex(pts):
    angle_sum = 0
    for i in range(4):
        a = pts[i][0]
        b = pts[(i+1)%4][0]
        c = pts[(i+2)%4][0]
        # b is center
        value = numpy.dot(a-b,c-b)
        if (a == b).all() or (b==c).all():
            return False
        value/=(numpy.sqrt(numpy.dot(a-b,a-b))*(numpy.sqrt(numpy.dot(c-b,c-b))))
        if value<-1 or value>1:
            return False
        angle = numpy.arccos(value)/numpy.pi*180
        angle_sum+=angle
        if angle>180:
            return False
    tmp = list(pts.reshape([4,2]))
    if np.abs(angle_sum-360)>1:
        return False
    if intersect(tmp[0],tmp[1],tmp[2],tmp[3])==False:
        return True
    else:
        return False

def process1(scaled_img):
    gray_img = cv2.medianBlur(scaled_img, 3)
    gray_img = cv2.GaussianBlur(gray_img, (3, 3), 0)
    for i in range(7):
        gray_img = cv2.medianBlur(gray_img, 15)
        gray_img = cv2.GaussianBlur(gray_img, (3, 3), 0)
    # gray_img = cv2.pyrMeanShiftFiltering(gray_img, 35, 50)
    gray_img = cv2.cvtColor(gray_img, cv2.COLOR_BGR2GRAY)
    gray_img = gray_img.astype(np.uint8)
    edges = cv2.Canny(gray_img, 4, 64)

    kernel = numpy.ones(MORPH_KERNEL_SIZE, dtype=numpy.uint8)
    closed = edges
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    #cv2.imshow('closed', closed)
    cv2.waitKey(0)
    return closed


def process2(scaled_img):
    median_blurred = cv2.medianBlur(scaled_img, 7)
    #cv2.imshow('median blurred', median_blurred)
    mean_shifted_image = cv2.pyrMeanShiftFiltering(median_blurred, 35, 50)
    mean_shifted_image = cv2.pyrMeanShiftFiltering(mean_shifted_image, 35, 50)
    #cv2.imshow('mean shifted', mean_shifted_image)
    gray_img = cv2.cvtColor(mean_shifted_image, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.GaussianBlur(gray_img, (BLUR_RADIUS, BLUR_RADIUS), 0)
    #cv2.imshow('gaussian blurred', gray_img)
    edges = cv2.Canny(gray_img, 16, 64)
    cv2.imshow('edges', edges)

    kernel = numpy.ones(MORPH_KERNEL_SIZE, dtype=numpy.uint8)
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    return closed

def findContours(scaled_img,gray_img,min_value=None,max_value=None,arc_length=DEFAULT_ARC_LENGTH):
    contours = cv2.findContours(gray_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
    # loop over the contours
    approx_rects = []
    potential_rects = []

    for contour in contours:
        # approximate the contour

        # contour_as_poly = numpy.array([[x[0] for x in contour]])
        # cv2.polylines(scaled_img, contour_as_poly, True, (0, 255, 0), thickness=2)
        # cv2.imshow('scaled_img',scaled_img)
        # cv2.waitKey()
        peri = cv2.arcLength(contour, True)
        approx_poly = cv2.approxPolyDP(contour,
                                       arc_length * peri,
                                       # 5,
                                       True)

        if len(approx_poly) == 4:
            isValid = True
            if min_value is not None or max_value is not None:
                for i in range(4):
                    length = numpy.sqrt(numpy.sum((approx_poly[i] - approx_poly[(i + 1) % 4]) ** 2))
                    occupy_scale = length / ((scaled_img.shape[0] + scaled_img.shape[1]) / 2.0)
                    if min_value is not None and occupy_scale < min_value:
                        isValid = False
                        break
                    if max_value is not None and occupy_scale > max_value:
                        isValid = False
                        break
            if isValid and check_convex(approx_poly):
                approx_rects.append(approx_poly)

        else:

            approx_poly = generate_rect(approx_poly)
            isValid = True
            if min_value is not None or max_value is not None:
                for i in range(4):
                    length = numpy.sqrt(numpy.sum((approx_poly[i] - approx_poly[(i + 1) % 4]) ** 2))
                    occupy_scale = length / ((scaled_img.shape[0] + scaled_img.shape[1]) / 2.0)
                    if min_value is not None and occupy_scale < min_value:
                        isValid = False
                        break
                    if max_value is not None and occupy_scale > max_value:
                        isValid = False
                        break
            if isValid and check_convex(approx_poly):
                potential_rects.append(approx_poly)
    return approx_rects,potential_rects

def generate_rect(polygon):

    convex_hull = cv2.convexHull(numpy.array(polygon))
    center, (w, h), theta = cv2.minAreaRect(convex_hull)
    theta = theta / 180 * numpy.pi

    rect_pts = numpy.array(
        [
            [-w/2, -h/2],
            [-w/2, h/2],
            [w/2, h/2],
            [w/2, -h/2]
        ]
    )

    M_rot = numpy.array(
        [
            [numpy.cos(theta), -numpy.sin(theta)],
            [numpy.sin(theta), numpy.cos(theta)]
        ]
    )

    return numpy.array([[numpy.dot(M_rot, x)+center] for x in rect_pts])


def get_outline(img, min_value=None, max_value=None,arc_length=DEFAULT_ARC_LENGTH):
    # gray_img = numpy.min(img, axis=2)  # if bg is black, use max()

    scale = float(EDGE_LIMIT) / max(img.shape[:2])
    if scale > 1:
        scale = 1

    scaled_img = cv2.resize(img, (0, 0), fx=scale, fy=scale)


    #gray_img = cv2.cvtColor(scaled_img, cv2.COLOR_BGR2GRAY)
    #gray_img = cv2.blur(gray_img, (3, 3))
    processed_img = process1(scaled_img)
    approx_rects1, potential_rects1 = findContours(scaled_img, processed_img, min_value, max_value, arc_length)
    processed_img = process2(scaled_img)
    approx_rects2,potential_rects2 = findContours(scaled_img,processed_img,min_value,max_value,arc_length)

    approx_rects =[]
    potential_rects = []
    for poly2 in approx_rects2:
        if len(poly2) == 4:
            approx_rects.append(poly2)

    for poly2 in potential_rects2:
        if len(poly2) == 4:
            potential_rects.append(poly2)

    for poly1 in approx_rects1:
        interSect = False
        poly1 = poly1.reshape([4,2])
        for poly2 in approx_rects2:
            if interSect:
                break
            poly2 = poly2.reshape([4,2])
            for i in range(4):
                if interSect:
                    break
                summ = 0
                for j in range(4):
                    up = np.dot(poly1[i,:]-poly2[j,:],poly1[i,:]-poly2[(j+1)%4,:])
                    down =  np.sqrt(np.sum((poly1[i,:]-poly2[j,:])**2))* \
                            np.sqrt(np.sum((poly1[i, :] - poly2[(j+1)%4, :]) ** 2))
                    angle = np.arccos(up/down)/np.pi*180
                    summ+=angle
                if np.abs(summ-360)<1:
                    interSect = True
                    break
            for i in range(4):
                if interSect:
                    break
                summ = 0
                for j in range(4):
                    up = np.dot(poly2[i, :] - poly1[j, :], poly2[i, :] - poly1[(j + 1) % 4, :])
                    down = np.sqrt(np.sum((poly2[i, :] - poly1[j, :]) ** 2)) * \
                           np.sqrt(np.sum((poly2[i, :] - poly1[(j + 1) % 4, :]) ** 2))
                    angle = np.arccos(up / down) / np.pi * 180
                    summ += angle
                if np.abs(summ - 360) < 1:
                    interSect = True
                    break
        if interSect == False:
            if len(poly1)==4:
                poly1 = poly1.reshape([4,1,2])
                approx_rects.append(poly1)

    for poly1 in potential_rects1:
        interSect = False
        poly1 = poly1.reshape([4, 2])
        for poly2 in potential_rects2:
            if interSect:
                break
            poly2 = poly2.reshape([4, 2])
            for i in range(4):
                if interSect:
                    break
                summ = 0
                for j in range(4):
                    up = np.dot(poly1[i, :] - poly2[j, :], poly1[i, :] - poly2[(j + 1) % 4, :])
                    down = np.sqrt(np.sum((poly1[i, :] - poly2[j, :]) ** 2)) * \
                           np.sqrt(np.sum((poly1[i, :] - poly2[(j + 1) % 4, :]) ** 2))
                    angle = np.arccos(up / down) / np.pi * 180
                    summ += angle
                if np.abs(summ - 360) < 1:
                    interSect = True
                    break
            for i in range(4):
                if interSect:
                    break
                summ = 0
                for j in range(4):
                    up = np.dot(poly2[i, :] - poly1[j, :], poly2[i, :] - poly1[(j + 1) % 4, :])
                    down = np.sqrt(np.sum((poly2[i, :] - poly1[j, :]) ** 2)) * \
                           np.sqrt(np.sum((poly2[i, :] - poly1[(j + 1) % 4, :]) ** 2))
                    angle = np.arccos(up / down) / np.pi * 180
                    summ += angle
                if np.abs(summ - 360) < 1:
                    interSect = True
                    break
        if interSect == False:
            if len(poly1) == 4:
                poly1 = poly1.reshape([4, 1, 2])
                approx_rects.append(poly1)


    # cv2.imshow('polys', scaled_img)
    # cv2.waitKey()

    outlines = numpy.array([[((x[0] + 0.5) / scale).astype(numpy.int32) for x in poly] for poly in approx_rects])
    potential_outlines = numpy.array(
        [[((x[0] + 0.5) / scale).astype(numpy.int32) for x in poly] for poly in potential_rects])
    return outlines, potential_outlines

def test_pinjie_dir(root='dst_pinjie',min_value=None,max_Value=None):
    lst = os.listdir(root)
    out_dir = os.path.join(root,'test')
    img_dir = os.path.join(root,'img')
    if os.path.exists(out_dir)==False:
        os.mkdir(out_dir)
    if os.path.exists(img_dir)==False:
        os.mkdir(img_dir)
    for e in lst:
        if e.endswith('.jpg'):
            index = 0
            path = os.path.join(root,e)
            image = cv2.imread(path,1)
            outlines, potential_outlines = get_outline(image)

            cv2.polylines(image, outlines, True, (0, 255, 0), thickness=9)
            cv2.polylines(image, potential_outlines, True, (255, 0, 0), thickness=9)
            cv2.imshow('img',image)
            cv2.waitKey(0)
            #cv2.imwrite(os.path.join(out_dir,e), image)

            fpath = os.path.join(root,e[:-3]+'txt')
            #f = open(fpath,'w')
            for outline in outlines:
                minx,miny = np.min(outline,0)
                maxx,maxy = np.max(outline,0)
                lenx = maxx-minx
                leny = maxy-miny
                minx+=int(lenx*0.1)
                miny+=int(leny*0.1)
                maxx-=int(lenx*0.1)
                maxy-=int(leny*0.1)
                cv2.imwrite(os.path.join(img_dir,e[:-3]+'_'+str(index)+'.jpg'),image[miny:maxy,minx:maxx,:])
                index+=1
                # for pt in outline:
                #     f.write('%d,%d '%(pt[0],pt[1]))
                # f.write('\n')
            #f.close()
            print('%s Done' % fpath)
            print('%s Done'%path)

def cut_img_from_src(srcdir,desdir,min_value=None,max_value=None,):
    if os.path.exists(desdir) == False:
        os.mkdir(desdir)
    lst = os.listdir(srcdir)
    for e in lst:
        if e.endswith('.jpg'):
            path = os.path.join(srcdir, e)
            image = cv2.imread(path,1)
            outlines, potential_outlines = get_outline(image,min_value,max_value)
            outlines = list(np.array(outlines).reshape([-1,4,1,2]))
            rectangles = [cv2.minAreaRect(outline) for outline in outlines]
            for outline in outlines:
                rectangle = cv2.minAreaRect(rectangle)
                points = cv2.boxPoints(rectangle)
                cv2.PerspectiveTransform(outline, points)
                cv2.warpPerspective()

            #cvWarpPerspective(srcImg, dstImg, warp_mat, CV_INTER_LINEAR, cvScalarAll(255))
            for rectangle in rectangles:
                points = cv2.boxPoints(rectangle)
                cv2.rectangle(image,(points[0][0],points[0][1]),(points[2][0],points[2][1]),color=(0,0,255))
            cv2.imwrite(os.path.join(desdir,e), image)

if __name__ == '__main__':
    #test_pinjie_dir()
    #test_pinjie_image(src_path=r'C:\Users\ludongwei\Desktop\photo_pinjie\test.jpg', out_path=r'C:\Users\ludongwei\Desktop\photo_pinjie\test')
    #cut_img_from_src(r'C:\Users\ludongwei\Desktop\photo_pinjie',r'C:\Users\ludongwei\Desktop\photo_pinjie\test',0.07,0.85)
    test_pinjie_dir(r'E:\data\618data\concat\pos',0.05,0.85
                    )# )
    #test_Hough(r'C:\Users\ludongwei\Desktop\photo_pinjie')

