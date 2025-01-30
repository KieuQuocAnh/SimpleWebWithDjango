from django.db import models  # Thư viện models của Django để định nghĩa các model
from django.utils import timezone  # Thư viện timezone để làm việc với thời gian
from django.contrib.auth.models import User  # Model User của Django để liên kết bài viết với người dùng
from django.urls import reverse  # Hàm reverse dùng để tạo URL động dựa trên tên URL

class Post(models.Model):
    # Định nghĩa các thuộc tính của model Post
    
    title = models.CharField(max_length=100)  # Trường tiêu đề, giới hạn tối đa 100 ký tự
    content = models.TextField()  # Trường nội dung không giới hạn độ dài
    date_posted = models.DateTimeField(default=timezone.now)  # Thời gian đăng bài, mặc định là thời gian hiện tại
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    # Thiết lập mối quan hệ với User. Khi User bị xóa, các bài viết của họ cũng sẽ bị xóa theo 
    like = models.BooleanField(default=False)
    like_count = models.PositiveIntegerField(default=0)
    # Thiết lập mối quan hệ với User. Khi User bị xóa, các bài viết của họ cũng sẽ bị xóa theo (on_delete=models.CASCADE).

    def __str__(self):
        # Phương thức trả về chuỗi đại diện cho đối tượng Post, sẽ hiển thị tiêu đề bài viết khi in đối tượng Post ra
        return self.title

    def get_absolute_url(self):
        # Phương thức trả về URL chi tiết của bài viết
        # 'post-detail' là tên của URL trong urls.py, 'kwargs' chứa từ khóa với 'pk' (primary key) của bài viết hiện tại
        return reverse('post-detail', kwargs={'pk': self.pk})
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="comments",default='None')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=256,default='None')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:20]  # Hiển thị đoạn đầu của nội dung



class Like(models.Model):
    post= models.ForeignKey(Post,related_name='likes',on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
            unique_together=('post','user')#Đảm bảo mỗi user chỉ có thể like một bài viết một lần
