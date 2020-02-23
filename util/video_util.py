def make_video(outvid, images=None, fps=30, size=None, is_color=True, format="FMP4"):
    """
    Create a video from a list of images.

    @param      outvid      output video
    @param      images      list of images to use in the video
    @param      fps         frame per second
    @param      size        size of each frame
    @param      is_color    color
    @param      format      see http://www.fourcc.org/codecs.php
    @return                 see http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

    The function relies on http://opencv-python-tutroals.readthedocs.org/en/latest/.
    By default, the video will have the size of the first image.
    It will resize every image to this size before adding them to the video.
    """
    from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
    fourcc = VideoWriter_fourcc (*format)
    vid = None
    for image in images:
        if not os.path.exists (image):
            raise FileNotFoundError (image)
        img = imread (image)
        if vid is None:
            if size is None:
                size = img.shape[1], img.shape[0]
            vid = VideoWriter (outvid, fourcc, float (fps), size, is_color)
        if size[0] != img.shape[1] and size[1] != img.shape[0]:
            img = resize (img, size)
        vid.write (img)
    vid.release ()
    return vid


def make_video_from_directory(images_dir, output_video_dir, video_file_name):
    """
        Create a video from a list of images.

        @param      images_dir          Input images directory
        @param      output_video_dir    Output video directory
        @param      video_file_name     File Name.
    """
    import glob
    import os

    # Directory of images to run detection on
    images = list (glob.iglob (os.path.join (images_dir, '*.jpg')))

    # Sort the images by integer index
    images = sorted (images, key=lambda x: float (os.path.split (x)[1].split ("_")[0]))

    outvid = os.path.join (output_video_dir, video_file_name)
    make_video(outvid, images, fps=30)
