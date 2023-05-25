from rest_framework import permissions

class ReadOnlyPermission(permissions.BasePermission):
    '''Позволяет только читать данные.НЕ УДАЛЯТЬ!
    Удалять данные может только администратор'''

    #переопределяю метод has_permission, потому что делаю ограничение на уровне всего запроса:
    def has_permission(self, request, view):
        #проверяем что за запрос пришел от клиента (запрос на удаление или нет)
        if request.method in permissions.SAFE_METHODS:
            return True
        #а если все же запрос на удаление, то проверяем, если у пользователя права администратора:
        return bool(request.user and request.user.is_staff)