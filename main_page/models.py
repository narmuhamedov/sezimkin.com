from django.db import models


#about_me
class AboutME(models.Model):
    text_hobby = models.TextField('Напишите блог о своих увлечениях')
    text_work = models.TextField('Напишите блог о своей работе')
    text_secret = models.TextField('Напишите блог о ваших секретах')

    class Meta:
        verbose_name = 'информацию о себе'
        verbose_name_plural = 'Обо мне'

    def __str__(self):
        return f'Увлечение работа секреты'

class AboutMEPhoto(models.Model):
    image_about = models.ImageField('Добавьте фото в Блог о себе', upload_to='aboutMe')

    class Meta:
        verbose_name = 'название фото'
        verbose_name_plural = 'Фото в вкладке о себе'



#target
class Target(models.Model):
    target_future = models.TextField('Напишите блог об вашем ближайшем будущем')
    target_personal_live = models.TextField('Напишите блог об личной жизни')
    target_soul = models.TextField('Напишите блог об состоянии души')

    class Meta:
        verbose_name = 'цель'
        verbose_name_plural = 'Мои цели'

    def __str__(self):
        return f'Мои цели'




# logo #
class Logo(models.Model):
    logo = models.ImageField(upload_to='logo/')

    class Meta:
        verbose_name = 'логотип'
        verbose_name_plural = 'Логотип'

    def __str__(self):
        return f'Перейдите по ссылке !!!Внимание логотип не добавлять'

#galery#
class Slider(models.Model):
    image = models.ImageField(upload_to='sliders/')

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'Галерея'


    def __str__(self):
        return f'фотография'


#contact
class Contact(models.Model):
    instagram = models.URLField('Укажите ссылку на Instagram')
    telegram = models.URLField('Укажите ссылку на Telegram')
    whatsapp = models.URLField('Укажите ссылку на Whatsapp')
    address = models.CharField('Укажите город проживания', max_length=300)
    email = models.EmailField('Укажите вашу почту')
    number = models.CharField('Укажите ваш номер', max_length=15)

    class Meta:
        verbose_name = 'контактные данные'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'Перейдите по ссылке'