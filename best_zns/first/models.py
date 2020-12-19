from django.db import models

# Create your models here.
class Group(models.Model):
    group_name = models.CharField(max_length=20)

    def __str__(self):
        return self.text

class Social(models.Model):
    social_name = models.CharField(max_length=20)

    def __str__(self):
        return self.text

class User(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    social = models.ForeignKey(Social, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    #photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    birthdate = models.DateField()

    def __str__(self):
        return self.text

class Contact(models.Model):
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True)
    #photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    birthdate = models.DateField()
    favorite = models.BooleanField()
    HOT = 'HT'
    COLD = 'CLD'
    WARM = 'WRM'
    status_contact = (
        (HOT,'Hot'),
        (COLD,'Cold'),
        (WARM,'Warm'),
    )
    status = models.CharField(max_length=20, choices=status_contact,default=WARM)
    date_of_creating = models.DateField(auto_now_add=True)
    place_of_creation = models.CharField(max_length=100)
    group = models.CharField(max_length=20)
    priority = models.CharField(max_length=20)

    def __str__(self):
        return self.text

class Call(models.Model):
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    RECEIVED = 'RCVD'
    SKIPPED = 'SKPD'
    REJECTED = 'RJCD'
    call_status = (
        (RECEIVED,'Received'),
        (SKIPPED,'Skipped'),
        (REJECTED,'Rejected'),
    )
    status = models.CharField(max_length=20,choices=call_status) #Incoming or outgoing
    INCOMING = 'INCM'
    OUTCOMING = 'OTCM'
    types = (
        (INCOMING,'Incoming'),
        (OUTCOMING,'Outcoming'),
    )
    type_of_call = models.CharField(max_length=20,choices=types)
    additionally = models.CharField(max_length=100)
    audio = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.text

class SMS(models.Model):
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    RECEIVED = 'RCVD'
    SENT = 'SNT'
    DRAFT = 'DRFT'
    sms_status = (
        (RECEIVED,'Received'),
        (SENT,'Sent'),
        (DRAFT,'Draft'),
    )
    status = models.CharField(max_length=20, choices=sms_status) #Received\Sent/Draft
    INCOMING = 'INCM'
    OUTCOMING = 'OTCM'
    sms_type = (
        (INCOMING,'Incoming'),
        (OUTCOMING,'Outcoming'),
    )
    type = models.CharField(max_length=20,choices=sms_status)
    additionally = models.CharField(max_length=100)
    attachment = models.CharField(max_length=100)
    message = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.text

class Note(models.Model):
    heading = models.CharField(max_length=20)
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="notes")
    linked_contact = models.ForeignKey(Profile, on_delete=models.CASCADE)   #уточнить!
    place_of_creation = models.CharField(max_length=100)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class File(models.Model):
    heading = models.CharField(max_length=20)
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="files")
    linked_contact = models.ForeignKey(Profile, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class Phone(models.Model):
    phone = models.CharField(max_length=20)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Address(models.Model):
    address = models.CharField(max_length=100)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Email(models.Model):
    email = models.CharField(max_length=100)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Site(models.Model):
    site = models.CharField(max_length=100)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Work(models.Model):
    work = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Account(models.Model):
    social_id = models.ForeignKey(Social, on_delete=models.CASCADE)
    social_user = models.CharField(max_length=100)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Tag(models.Model):
    tag = models.CharField(max_length=20)
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Access(models.Model):
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    edit = models.BooleanField()

    def __str__(self):
        return self.text
