from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import (UserLoginForm,
                    UserRegisterForm,
                     UserUpdateForm,
                     ProfileUpdateForm,
                      
                  
                     PasswordChangingForm)


from django.contrib.auth import logout

from django.contrib.auth.views import PasswordChangeView,LoginView
from django.urls import reverse_lazy




class UserLoginView(LoginView):
    template_name = 'users/login.html'  # Template chứa giao diện form
    form_class = UserLoginForm  # Sử dụng form bạn đã định nghĩa

    def form_valid(self, form):
        # Thực thi khi form hợp lệ
   
        return super().form_valid(form)
    def get_form_kwargs(self):
        # Truyền thêm request vào form
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    def get_success_url(self):
        # Chuyển hướng sau khi đăng nhập thành công
        return reverse_lazy('blog-home')  # Thay 'home' bằng tên URL của bạn
    

# View xử lý đăng ký người dùng mới
def register(request):
    # Kiểm tra xem phương thức yêu cầu có phải là POST không (nghĩa là người dùng đang gửi form)
    if request.method == 'POST':
        # Tạo form từ dữ liệu POST
        form = UserRegisterForm(request.POST)
        # Kiểm tra xem dữ liệu gửi lên có hợp lệ không
        if form.is_valid():
            # Nếu hợp lệ, lưu người dùng mới vào cơ sở dữ liệu
            form.save()
            # Lấy tên người dùng vừa đăng ký thành công để hiện trong thông báo
            username = form.cleaned_data.get('user_name')
            # Thông báo thành công cho người dùng
            messages.success(request, f'Your account has been created! You are now able to log in')
            # Chuyển hướng người dùng đến trang đăng nhập
            return redirect('login')
    else:
        # Nếu không phải là POST, tạo form trống để hiển thị cho người dùng điền thông tin
        form = UserRegisterForm()
    # Render trang đăng ký với form
    return render(request, 'users/register.html', {'form': form})


# View xử lý hồ sơ cá nhân của người dùng (yêu cầu phải đăng nhập)
@login_required
def profile(request):
    # Kiểm tra xem yêu cầu có phải là POST không (người dùng đang cập nhật thông tin)
    if request.method == 'POST':
        # Khởi tạo form cập nhật thông tin người dùng từ dữ liệu POST và gán instance là user hiện tại
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # Khởi tạo form cập nhật profile từ dữ liệu POST và FILES (cập nhật hình ảnh), gán instance là profile hiện tại
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        
        # Kiểm tra xem cả hai form có hợp lệ không
        if u_form.is_valid() and p_form.is_valid():
            # Nếu hợp lệ, lưu thông tin cập nhật của user và profile
            
            u_form.save()
            p_form.save()
      
            # Thông báo thành công khi cập nhật
            # messages.success(request, f'Your account has been updated!')
            # Chuyển hướng người dùng về lại trang profile sau khi cập nhật thành công
            return redirect('profile')
    else:
        # Nếu không phải POST, tạo form với dữ liệu người dùng hiện tại (hiển thị thông tin người dùng để chỉnh sửa)
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
       

    # Tạo context chứa cả hai form để truyền vào template
    context = {
        'u_form': u_form,
        'p_form': p_form,
      
    }

    # Render trang hồ sơ cá nhân với các form
    return render(request, 'users/profile.html', context)



#PASSWORD CHANGE VIEWS
#đây là cách ta tự tạo 1 class riêng để có thể chỉnh sửa mà không dùng cái mặc định của djangodjango


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm # Dùng form mặc định của Django
    success_url= reverse_lazy('password_success')

def logout_user(request):
    logout(request)
    
    return redirect('login')
def password_success(request):
    logout(request)
    messages.success(request,("Your Password Was Changhed Successfully... "))
    return redirect('login')
