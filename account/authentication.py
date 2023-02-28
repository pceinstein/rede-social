from django.contrib.auth.models import User


class EmailAuthBackend(object):
    '''
        Faz autenticação usando endereço de email
    '''

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            # check_password é um método embutido do modelo de usuário
            # que cuida do hashing da senha para comparar com a senha
            # armazenada no banco de dados
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None