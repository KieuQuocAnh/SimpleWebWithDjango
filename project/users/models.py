from PIL import Image  # Import thư viện xử lý ảnh Pillow
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator

class Profile(models.Model):
    user_acount_name = models.OneToOneField(User, on_delete=models.CASCADE)
    is_logged_in = models.BooleanField(default=False)
    user_name=models.CharField(max_length=50, null=True,blank=True)  # Default sẽ thay đổi sau
    PR_content = models.TextField(validators=[],null=True,blank=True)  # Giới hạn độ dài nội dung tối đa 75 ký tự
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    

    def __str__(self):
        return f'{self.user_acount_name.username} Profile'

    # Ghi đè phương thức save của model
    def save(self, *args, **kwargs):
        # Gọi phương thức save của lớp cha để đảm bảo dữ liệu được lưu vào cơ sở dữ liệu trước
        super().save(*args, **kwargs)

        # Mở tệp ảnh vừa lưu để kiểm tra kích thước
        img = Image.open(self.image.path)

        # Kiểm tra xem ảnh có lớn hơn kích thước mong muốn (300x300) hay không
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # Tạo thumbnail với kích thước 300x300
            img.thumbnail(output_size)
            # Lưu ảnh lại với đường dẫn ban đầu
            img.save(self.image.path)



