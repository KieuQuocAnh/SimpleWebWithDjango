        // Khi người dùng nhấn vào nút tùy chỉnh, kích hoạt sự kiện chọn file
        document.querySelector('.custom-upload-button').addEventListener('click', function() {
            document.querySelector('input[type="file"]').click(); // Kích hoạt input file
        });

        // Thay đổi nội dung của nút khi chọn file
        document.querySelector('input[type="file"]').addEventListener('change', function(e) {
            var label = document.querySelector('.custom-upload-button');
            if (e.target.files.length > 0) {
                label.innerText = e.target.files[0].name; // Hiển thị tên file đã chọn
            } else {
                label.innerText = 'Choose Your Image'; // Nếu không chọn file, hiển thị lại nội dung ban đầu
            }
        });