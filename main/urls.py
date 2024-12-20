from django.urls import path
from main.views import show_main, create_games_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_game, delete_game, add_game_entry_ajax
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-games-entry', create_games_entry, name='create_games_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-game/<uuid:id>', edit_game, name='edit_game'),
    path('delete/<uuid:id>', delete_game, name='delete_game'),
    path('create-games-entry-ajax', add_game_entry_ajax, name='add_game_entry_ajax'),
    path('auth/', include('authentication.urls')),
    path('create-flutter/', create_game_flutter, name='create_game_flutter'),
]