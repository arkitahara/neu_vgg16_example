import numpy as np
import skimage
from skimage.transform import resize
from tensorflow.keras.applications.vgg16 import preprocess_input

def image_tensor(image):
    """ Convert grayscale image to keras tensor appropriate for the VGG model. 
    Args:
        image (numpy array): image data expected to be grayscale
    
    Returns:
        preprocessed_tensor (numpy array): output tensor ready to be processed by VGG16

    Notes:
        This function
            - reads an image (shape=(X,Y))
            - converts to ubyte
            - converts to RGB (shape=(X,Y,3))
            - converts to `dtype=np.float32`
            - expands dimensions along axis 0 (shape=(1,X,Y,3))
            - applies VGG16 preprocessing (subtract mean values over the ImageNet dataset from each channel)
    """

    # yield an RGB image on the range [0.0,255.0]
    # convert to ubyte (integer on range [0,255])
    image = skimage.img_as_ubyte(image)

    # copy grayscale image onto color channels
    image3d = skimage.color.gray2rgb(image)

    # convert to floating point
    image3d = image3d.astype(np.float32)

    # add the sample dimension to the array
    x = np.expand_dims(image3d, axis=0)

    # keras.applications.vgg16.preprocess_input
    # subtract mean values over the ImageNet dataset from each channel
    preprocessed_tensor = preprocess_input(x)
    
    return preprocessed_tensor


def process_image(image, input_size=224):
    """Perform all necessary preprocessing of an image for VGG16.
    Args:
        image (numpy array): assume grayscale image of arbitrary square size
        input_size (int): standard size to resize image to (default=224 for VGG16)
    
    Returns:
        tensor_output (numpy array): fully preprocessed tensor

    Notes:
        - This function resizes the image to (input_size x input_size)
        - Then it applies the `image_tensor` function (inside this module)
    
    Requirements:
        - `skimage`
    """
    image = resize(image, (input_size, input_size))
    tensor_output = image_tensor(image)
    return tensor_output