from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# 이렇게 User 객체 참조해서는 안됨!
# from .models import User

# UserCreationForm()은 유저 모델을 커스텀했기 때문에 바로 사용하지 못하고
# 유저 커스텀 모델을 새롭게 등록해야 함
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 현재 django 프로젝트에 활성화된 User 객체를 자동으로 반환하는 함수
        # 당장 이름 바꾸어도 참조하는 User 객체 바뀌지 않음
       model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)