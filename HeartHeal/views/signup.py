from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from HeartHeal.models.user import User, Examination

from django.views import View

def collect_exam(request): 
    text_list = []
    text_list.append("1. Đâu là loại hình liệu pháp điều trị bạn tìm kiếm?")
    text_list.append("-" + request.POST['lieu_phap'])
    text_list.append("2. Giới tính sinh học của bạn là gì?")
    text_list.append("-" + request.POST['gioi_tinh_sinh_hoc'])
    text_list.append("3. Độ tuổi của bạn ở thời điểm hiện tại là bao nhiêu?")
    text_list.append("-" + request.POST['tuoi'])
    text_list.append("4. Thiên hướng giới tính phù hợp nhất để mô tả bạn là gì?")
    text_list.append("-" + request.POST['thien_huong_gioi_tinh'])
    text_list.append("5. Trạng thái tình cảm của bạn là gì?")
    text_list.append("-" + request.POST['trang_thai_tinh_cam'])
    text_list.append("6. Bạn có phải người theo đạo không?")
    text_list.append("-" + request.POST['theo_dao_khong'])
    text_list.append("7. Bạn đã từng trải qua trị liệu tâm lý chưa?")
    text_list.append("-" + request.POST['da_chua'])
    text_list.append("8. Đâu là lý do đưa bạn đến đây ngày hôm nay?")
    tai_sao_den = request.POST.getlist('tai_sao_den')
    for li_do in tai_sao_den:
        text_list.append("-" + li_do)
    text_list.append("9. Mong muốn của bạn với chuyên gia tư vấn trị liệu cho mình là một người thế nào?")
    bac_si_nhu_nao = request.POST.getlist('bac_si_nhu_nao')
    for nhu_nao in bac_si_nhu_nao:
        text_list.append("-" + nhu_nao)
    text_list.append("10. Bạn đánh giá thể trạng sức khỏe của mình ra sao?")
    text_list.append("-" + request.POST['suc_khoe'])
    text_list.append("11. Bạn đánh giá tình hình ăn uống của mình ra sao?")
    text_list.append("-" + request.POST['an_uong'])
    text_list.append("12. Bạn có đang trải qua cảm giác đau buồn, tiếc nuối, bi thương và u uất không? ")
    text_list.append("-" + request.POST['dau_buon'])
    text_list.append("13. Trong 2 tuần qua, tần suất bạn bị ảnh hưởng bởi những cảm xúc này: Không có hứng thú hay thỏa mãn khi làm mọi việc")
    text_list.append("-" + request.POST['ko_hung_thu'])
    text_list.append("14. Cảm thấy tệ về bản thân - cảm giác bạn là kẻ thất bại hoặc đã khiến bản thân và gia đình thất vọng")
    text_list.append("-" + request.POST['ban_than_te'])
    text_list.append("15. Tập trung vào hai việc cùng một lúc, ví dụ như cùng lúc học, cùng lúc xem phim")
    text_list.append("-" + request.POST['hai_viec_mot_luc'])
    text_list.append("16. Có suy nghĩ bản thân nên chết đi hoặc tự làm tổn thương bản thân theo các cách khác nhau")
    text_list.append("-" + request.POST['tu_hai_minh'])
    text_list.append("17. Mức độ khó khăn đến từ những vấn đề trên cho việc hoàn thành công việc, chăm lo việc nhà, hoặc giao lưu cùng người khác của bạn?")
    text_list.append("-" + request.POST['kho_khan_lam_viec'])
    text_list.append("18. Bạn có vấn đề hoặc lo lắng về sự thân mật?")
    text_list.append("-" + request.POST['than_mat'])
    text_list.append("19. Bạn có thường xuyên uống đồ có cồn?")
    text_list.append("-" + request.POST['uong_do_co_con'])
    text_list.append("20. Đâu là lần cuối bạn nghĩ tới việc tự tử?")
    text_list.append("-" + request.POST['tu_sat'])
    text_list.append("21. Bạn có đang trải qua cảm giác lo lắng, cơn hoảng loạn (tim đập nhanh, choáng váng, đau bụng,...) hay ám ảnh sợ hãi?")
    text_list.append("-" + request.POST['lo_lang_hoang_loan'])
    text_list.append("22. Bạn có đang trong quá trình sử dụng thuốc?")
    text_list.append("-" + request.POST['su_dung_thuoc'])
    text_list.append("23. Bạn có đang mắc phải bất kỳ tình trạng bệnh mãn tính?")
    text_list.append("-" + request.POST['benh_man_tinh'])
    text_list.append("24. Bạn đánh giá mức độ tài chính cá nhân của mình ra sao?")
    text_list.append("-" + request.POST['tai_chinh_ca_nhan'])
    text_list.append("25. Bạn đánh giá chất lượng giấc ngủ của mình ra sao?")
    text_list.append("-" + request.POST['chat_luong_giac_ngu'])
    text_list.append("26. Đâu là liệu pháp bạn mong đợi và thấy hiệu quả?")
    lieu_phap_mong_doi = request.POST.getlist('lieu_phap_mong_doi')
    for lieu_phap in lieu_phap_mong_doi:
        text_list.append("-" + lieu_phap)
    text_list.append("27. Bạn có yêu cầu đặc biệt gì về chuyên gia tâm lý?")
    yeu_cau_chuyen_gia = request.POST.getlist('yeu_cau_chuyen_gia')
    for yeu_cau in yeu_cau_chuyen_gia:
        text_list.append("-" + yeu_cau)
    text_list.append("28. Bạn biết đến HeartHeal từ đâu?")
    text_list.append("-" + request.POST['sao_biet'])
    text_list.append("29. Tôi mong muốn chuyên gia hỗ trợ mình có kiến thức sâu về mảng dưới đây")
    kien_ve_mang_nao = request.POST.getlist('kien_ve_mang_nao')
    for chuyenmon in kien_ve_mang_nao:
        text_list.append("-" + chuyenmon)

    text = "\n".join(text_list)
    return text

class Signup(View):
    def get(self, request):
        if('user' not in request.session):
            return render(request, 'signup.html')
        return redirect('dashboard')

    def post(self, request):
        postData = request.POST
        name = postData.get('name')
        phone = postData.get('phone')
        email = postData.get('email')
        password1 = postData.get('password1')
        password2 = postData.get('password2')
        # validation
        value = {
            'name': name,
            'phone': phone,
            'email': email
        }
        error_message = None

        user = User(name=name, phone=phone, email=email, password=password1)
        error_message = self.validateUser(user, password2)

        if not error_message:
            print(name, phone, email, password1)
            user.password = make_password(user.password)
            user.register()

            # save mental status examination of the patient
            mental_status = collect_exam(request)
            exam = Examination(patient=user, content = mental_status)
            exam.save()
            request.session['user'] = user.id
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateUser(self, user, verify_password):
        error_message = None
        if (not user.name):
            error_message = "Please Enter your Name !!"
        elif(user.password != verify_password):
            error_message = "Password didn't match !!"
        elif not user.phone:
            error_message = 'Enter your Phone Number'
        elif len(user.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(user.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len(user.email) < 5:
            error_message = 'Email must be 5 char long'
        elif user.is_Exists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message