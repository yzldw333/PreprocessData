import numpy
import cv2
BLUR_RADIUS = 3
MORPH_KERNEL_SIZE = (11, 11)
DEFAULT_ARC_LENGTH = 0.09
EDGE_LIMIT = 800

def check_convex(pts):
    for i in range(4):
        a = pts[i]
        b = pts[(i+1)%4]
        c = pts[(i+2)%4]
        # b is center
        angle = numpy.arcos(numpy.dot((a-b)*(c-b))*1.0/(numpy.sqrt(sum((a-b)**2))*(numpy.sqrt(sum((c-b)**2)))))
        if angle>numpy.pi:
            return False
    return True

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


def get_outline(img, arc_length=DEFAULT_ARC_LENGTH):
    #gray_img = numpy.min(img, axis=2)  # if bg is black, use max()

    scale = float(EDGE_LIMIT) / max(img.shape[:2])
    if scale > 1:
        scale = 1

    scaled_img = cv2.resize(img, (0, 0), fx=scale, fy=scale)
    gray_img = cv2.cvtColor(scaled_img, cv2.COLOR_BGR2GRAY)

    gray_img = cv2.medianBlur(gray_img, 7)
    #cv2.imshow('median blurred', gray_img)
    gray_img = cv2.GaussianBlur(gray_img, (BLUR_RADIUS, BLUR_RADIUS), 0)
    #cv2.imshow('gaussian blurred', gray_img)

    edges = cv2.Canny(gray_img, 16, 64)
    #cv2.imshow('edges', edges)

    kernel = numpy.ones(MORPH_KERNEL_SIZE, dtype=numpy.uint8)
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    #cv2.imshow('closed', closed)


    contours = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

    # loop over the contours
    approx_rects = []
    potential_rects = []

    for contour in contours:
        # approximate the contour

        contour_as_poly = numpy.array([[x[0] for x in contour]])
        cv2.polylines(scaled_img, contour_as_poly, True, (0, 255, 0), thickness=2)

        peri = cv2.arcLength(contour, True)
        approx_poly = cv2.approxPolyDP(contour, arc_length * peri, True)

        if len(approx_poly) == 4:
            approx_rects.append(approx_poly)

        else:
            potential_rects.append(generate_rect(approx_poly))

    #cv2.imshow('polys', scaled_img)
    #cv2.waitKey()

    outlines = numpy.array([[((x[0]+0.5)/scale).astype(numpy.int32) for x in poly] for poly in approx_rects])
    potential_outlines = numpy.array([[((x[0]+0.5)/scale).astype(numpy.int32) for x in poly] for poly in potential_rects])
    return outlines, potential_outlines



if __name__ == '__main__':

    image = cv2.imread(r'C:\Users\ludongwei\Desktop\photo_pinjie\IMG_20170417_133856.jpg')
    outlines, potential_outlines = get_outline(image)

    cv2.polylines(image, outlines, True, (0, 255, 0), thickness=9)
    cv2.polylines(image, potential_outlines, True, (255, 0, 0), thickness=9)


    for pt0, _, pt1,__ in outlines:
        pts = numpy.array([pt0,_,pt1,__])
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, pts,True,(0, 255, 0), 9)

    for pt0, _, pt1, _ in potential_outlines:
        pts = numpy.array([pt0, _, pt1, __])
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, pts, True,(255,0, 0), 9)


    cv2.imwrite(r'C:\Users\ludongwei\Desktop\photo_pinjie\test\test.jpg', image)
