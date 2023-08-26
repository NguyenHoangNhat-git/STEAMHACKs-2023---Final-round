const contentBox = document.getElementById('therapy-text-content')

document.querySelector('#tam-dong-hoc').addEventListener('click', function() {
    contentBox.innerHTML = "1. Giúp khách hàng khám phá bản thân bằng cách tìm hiểu những tầng nghĩ vô thức của các hành động mình thực hiện, từ đó làm thay đổi cách tư duy, cảm nhận và hành xử có vấn đề của người bệnh"
});

document.querySelector('#hanh-vi').addEventListener('click', function() {
    contentBox.innerHTML = "2. Giúp khách hàng xác định và thay đổi những hành vi tiêu cực qua việc tập trung vào vấn đề và môi trường dẫn tới hành động của họ."
});

document.querySelector('#nhan-thuc').addEventListener('click', function() {
    contentBox.innerHTML = "3. Giúp khách hàng khám phá dạng thức suy nghĩ của mình để loại bỏ cách suy nghĩ tiêu cực và bất ổn nhằm tránh hành động cực đoan gây ra bởi kiểu tư duy này, từ đó dẫn đến kiểu suy nghĩ và hành xử lành mạnh"
});

document.querySelector('#nhan-van').addEventListener('click', function() {
    contentBox.innerHTML = "4. Giúp khách hàng có khả năng đạt đến những tiềm năng hoàn chỉnh nhất của bản thân nhờ nuôi dưỡng đúng cách qua việc tập trung vào công cuộc tìm kiếm ý nghĩa sống cho người bệnh."
});

document.querySelector('#tich-hop').addEventListener('click', function() {
    contentBox.innerHTML = "5. Quan tâm đến làm sao để mang lại kết quả điều trị tốt nhất cho khách hàng của mình, nên đôi lúc chuyên gia sẽ kết hợp nhiều phương pháp tâm lý trị liệu lại với nhau, từ đó đưa đến những kỹ thuật “thiết kế riêng” để giải quyết được bất kỳ khó khăn nào mà người bệnh có thể gặp phải."
});



