
from django.shortcuts import render ,get_object_or_404,redirect # Import hàm render để render HTML template với dữ liệu từ view
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # Import các mixin kiểm tra đăng nhập và quyền truy cập
from django.views.generic import (
                                 ListView,
                                 DetailView,
                                 CreateView,
                                 UpdateView,
                                 DeleteView
                                 )  # Import các class view để tạo view theo kiểu class-based view
from .models import Post,Comment,Like  # Import model Post từ file models để truy cập dữ liệu từ database
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post

class UserProfileView(DetailView):
    model = User 
    template_name = 'blog/user_profile_view.html'
    context_object_name = 'User'
    slug_field = 'username'
    slug_url_kwarg = 'username' 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        context['profile'] = user.profile  # Thêm profile vào context
        return context

   

class PostListView(ListView):
    model = Post  
    template_name = 'blog/home.html'  
    context_object_name = 'posts'  
    ordering = ['-date_posted']  
    paginate_by = 3 
    

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = Post.objects.annotate(
            comment_count=Count('comments')
        ).order_by('-date_posted')
        if query:
            return Post.objects.filter(title__icontains=query).order_by('-date_posted')
        return Post.objects.all().order_by('-date_posted')


        
class UserPostListView(ListView):  
    model = Post  # Đặt model là Post để truy vấn dữ liệu từ bảng Post
    
    template_name = 'blog/user_posts.html'  # Đường dẫn template sẽ được render
    context_object_name = 'posts'  # Tên biến dùng để truy cập dữ liệu post trong template
    paginate_by = 3
    

    # Lấy danh sách bài đăng của người dùng cụ thể và sắp xếp giảm dần theo ngày đăng
    def get_queryset(self):
        # Lấy đối tượng người dùng dựa trên username từ URL; trả về 404 nếu không tồn tại
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # Trả về danh sách các bài đăng của user, sắp xếp giảm dần theo ngày đăng
        return Post.objects.filter(author=user).order_by('-date_posted')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        context['profile'] = user.profile  # Thêm profile vào context
        return context

    
    

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Sắp xếp các bình luận từ mới đến cũ
        context['comments'] = self.object.comments.all().order_by('-date_posted')
        return context




# View cho việc xóa bài viết, yêu cầu người dùng đăng nhập và phải là tác giả của bài viết
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post  # Sử dụng model Post
    success_url = '/'  # Đường dẫn sau khi xóa bài viết thành công

    def test_func(self):  # Hàm kiểm tra quyền để đảm bảo chỉ tác giả mới có thể xóa bài viết
        post = self.get_object()  # Lấy bài viết hiện tại
        if self.request.user == post.author:  # Kiểm tra nếu người dùng hiện tại là tác giả
            return True
        return False  # Trả về False nếu người dùng không phải tác giả

# View cho việc tạo bài viết mới, yêu cầu người dùng đăng nhập

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post  # Sử dụng model Post
    form_class = PostForm  # Sử dụng form PostForm
    # fields = ['title', 'content']  # Chỉ định các trường sẽ được hiển thị trong form tạo bài viết
    template_name = 'blog/post_form.html'  # Tùy chỉnh template

    success_url = reverse_lazy('blog-home')  # Chuyển hướng sau khi tạo bài viết thành công

    def form_valid(self, form):  # Phương thức xác thực form trước khi lưu vào database
        form.instance.author = self.request.user  # Gán tác giả bài viết là người dùng hiện tại
        return super().form_valid(form)  # Gọi phương thức form_valid của lớp cha
    # def home(request):
   
    #     return render(request, 'blog/home.html')  # Render template 'blog/home.html' với context chứa các bài viết





# View cho việc cập nhật bài viết, yêu cầu người dùng đăng nhập và phải là tác giả của bài viết
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post  # Sử dụng model Post
    # fields = ['title', 'content']  # Chỉ cho phép cập nhật trường title và content
    form_class = PostForm
    template_name = 'blog/post_form.html'  # Tùy chỉnh template
    success_url = reverse_lazy('blog-home')  # Chuyển hướng sau khi cập nhật thành công
    def form_valid(self, form):  # Phương thức xác thực form trước khi lưu vào database
        form.instance.author = self.request.user  # Gán tác giả bài viết là người dùng hiện tại
        return super().form_valid(form)  # Gọi phương thức form_valid của lớp cha

    def test_func(self):  # Hàm kiểm tra quyền để đảm bảo chỉ tác giả mới có thể cập nhật bài viết
        post = self.get_object()  # Lấy bài viết hiện tại
        return self.request.user == post.author  # Kiểm tra nếu user là tác giả bài viết








# Thích bài viết
from django.contrib import messages
@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    # Check if the user has already liked this post
    like, created = Like.objects.get_or_create(user=user, post=post)
    if created:
        # The user is liking the post for the first time
        post.like_count += 1
        post.save()
        
    else:
        # If you want to allow users to unlike the post, you could delete the `Like` record here
        like.delete()
        post.like_count -= 1
        post.save()

    return redirect('post-detail', pk=pk)


from django.http import HttpResponse
def comment_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        comment_content = request.POST.get('comment', '').strip()
        if not comment_content:
            return HttpResponse("<script>alert('Comment cannot be empty!'); window.history.back();</script>")
        elif not request.user.is_authenticated:
            # return HttpResponse("<script>alert('You must be logged in to comment!'); window.history.back();</script>") câu lệnh này cungx ok nhưng thôi 
            # return render(template_name="users/login.html") câu lệnh này như cựt không nên dùng trong trường hợp này
            return redirect('login')
        else:
            Comment.objects.create(post=post, author=request.user, content=comment_content)
    return redirect('post-detail', pk=pk)

