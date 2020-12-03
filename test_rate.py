from image import Image
def test_rate_img_regular():
    image1 = Image('000001','Hamilton','none','user1')
    UserRate1 = 4
    UserRate2 = 3
    UserRate3 = 1
    UserRate4 = 4
    UserRate5 = 5
    image1.rate_img(UserRate1)
    image1.rate_img(UserRate2)
    image1.rate_img(UserRate3)
    image1.rate_img(UserRate4)
    image1.rate_img(UserRate5)
    assert image1.rates == [4,3,1,4,5],"these are regular rating scores"

def test_rate_img_exceptional():
    image2 = Image('000002','Hamilton','none','user1')
    UserRate1 = -4
    UserRate2 = -3
    UserRate3 = -1
    UserRate4 = 6
    UserRate5 = 999
    image2.rate_img(UserRate1)
    image2.rate_img(UserRate2)
    image2.rate_img(UserRate3)
    image2.rate_img(UserRate4)
    image2.rate_img(UserRate5)
    assert image2.rates == [-4,-3,-1,6,999], "these are exceptional ratings"

def test_rate_img_edge():
    image3 = Image('000003','Hamilton','none','user1')
    image3.rate_img(0)
    assert image3.rates == [0], "this is an edge case"

    image3.rate_img(5)
    assert image3.rates, "this is an edge case"