import FaceSet

key ="1Fvlr9BTd7BKVR1kN3pYfWzsoJTIqnJm"
secret ="6K9kMqHn-Rt5YxQDo0yd1z3cDOU4lO12"
kw = {'display_name':'demo' , 'outer_id':1 , 'tags':'person' , 'face_tokens':'c09fbffc73d8b8829fb496789a23a208,'    #胡歌
                                                                             '21aaf791b6da5f62d55ec0f1844a9d12,'    #梅西
                                                                             'ef243b455ed5b0d57f5232d6b0d9e488,'    #陈宇轩
                                                                             '1598429176a4712139f651ab86296342,'    #C罗
                                                                             '3d54e61832189a09ab5aa8f6eb9af16d'}    #内马尔
FaceSet.create(key,secret,kw)