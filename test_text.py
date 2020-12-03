from image import Image

def test_check_txt():
    image1 = Image('000001','none','this is an example image description this is an example image descriptionthis is an example image descriptionthis is an example image description','none')
    image1.check_txt()
  #  assert image1.txtvalid, "the description should be within 140 chars!!!"

    image2 = Image('000001','none','this is an example image description','none')
    image2.check_txt()
    assert image2.txtvalid, "if this test fail, debug the program"