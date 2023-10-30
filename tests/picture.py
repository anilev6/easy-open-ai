if __name__=='__main__':

    from easy_open_ai.models import PictureGenerator, pic_saver

    req='a candy'
    b64_json_string=PictureGenerator(req, format='b64_json').task()[0]
    pic_saver(b64_json_string,req)
