from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns=[
    path('',my_appHome.as_view(), name='home'),
    path('write_to_autor/', SearchByPhoto.as_view(), name='search_by_photo'),
    path('searching_by_name/', GetItemNameFromUser.as_view(), name='get_item_name'),
    path('result_with_photo/', PhotoAnswerPage.as_view(), name='result_with_photo'),
    path('thankyou/', Thanksfull.as_view(), name='thanksforvisit'),
    path('thankyoutoo/', Thanksfull_DELETE_NAME.as_view(), name='thanksforvisit2'),
    path('result_with_name/', ItemNameAnswerPage.as_view(), name='result_with_name'),
    path('terms_of_use/',cache_page(60) (Terms_of_Use.as_view()),name='Terms_of_use'),
    path('privacy_policy/',cache_page(60) (PrivacyPolicy.as_view()), name='Privacy_policy'),
    path('cookie_policy/',cache_page(60) (CookiePolicy.as_view()), name='Cookie_policy'),
    path('searching_dish/',FindYouDishHere.as_view(), name='search_dishes'),
    path('dish_price/',DishesResult.as_view(),name='prices_for_dish'),
    path('products_set/',ProductsSet.as_view(),name='items_set'),
    path('choose_markets_for_searching/',SetResults.as_view(),name='resultsofsets'),
    path('thanks/',Thanksfull_DELETE_SET.as_view(),name='thanks_set'),
    path('registration/',UserRegistration.as_view(),name='registr'),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/',logout_user,name='logout'),


    #url для REST API
    path('api/v1/mainpagelist/', MainPageAPI.as_view()),
    path('api/v1/sitepoliticslist/', SitePoliticsAPI.as_view()),
    path('api/v1/itemsfromdata/', ItemsInfoAPI.as_view()),
]

handler404=pageNotFound