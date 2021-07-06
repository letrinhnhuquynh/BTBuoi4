from test_class import *


user = File_Interact("user.txt")

ndung = ["NhungTran","MinhAnh","BichChau","TienDat","HongNguyen"]
user.write_file_line(ndung)

TrinhDo = File_Interact("TrinhDo .txt")
Bang_Cap = ["12","Dai Hoc","Cao dang","12","Cao dang"]
TrinhDo.write_file_from_list(Bang_Cap)


