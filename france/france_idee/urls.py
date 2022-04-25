from django.urls import path
from .views import *

urlpatterns = [
    path ('', home , name="home"),
    path ('login/', login_view , name='login_view'),
    path ('register/', register_view , name='register_view'),
    path ('logout/', logout_view, name='logout_view'),
    path ('hopital/', hopital_view, name='hopital_view'),
    path ('scolaire/', scolaire_view, name='scolaire_view'),
    path ('agriculture/', agriculture_view, name='agriculture_view'),
    path ('ajouter/', ajouter_view, name='ajouter_view'),
    path ('ajouterhopital/', ajouter_hopital_view, name='ajouter_hopital_view'),
    path ('ajouterscolaire/', ajouter_scolaire_view, name='ajouter_scolaire_view'),
    path ('ajouteragriculture/', ajouter_agriculture_view, name='ajouter_agricultures_view'),
    path ('<int:id>/updateh', ajouter_hopital_view, name='modif_hopital'),  # Modifie
    path ('<int:id>/updatea', ajouter_agriculture_view, name='modif_agriculture'),  # Modifie
    path ('<int:id>/updates', ajouter_scolaire_view, name='modif_scolaire'),  # Modifie
    path('deleteh/<int:id>', hopital_delete, name='hopital_delete'),
    path('deletes/<int:id>', scolaire_delete, name='scolaire_delete'),
    path('deletea/<int:id>', agriculture_delete, name='agriculture_delete'),
    path('likeh/<int:pk>', like_viewH, name='like_hopital'),
    path('likes/<int:pk>', like_viewS, name='like_scolaire'),
    path('likea/<int:pk>', like_viewA, name='like_agriculture'),

]