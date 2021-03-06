from django.db import models
from datetime import datetime
from django.utils import timezone
from api_integration.models import Student

class MessLeave(models.Model):
	leave_from=models.DateField(blank=True, null=True)
	leave_to=models.DateField(blank=True, null=True)
	student = models.ForeignKey('api_integration.Student', models.DO_NOTHING, blank=True, null=True)
	hometown=models.CharField(max_length=200)
	reason=models.TextField()
	ref_given = models.BooleanField(default = False)
	timestamp = models.DateTimeField(default=timezone.now())
	created_at = models.DateTimeField(blank=True, null=True)
	created_by = models.CharField(max_length=45, blank=True, null=True)
	modified_at = models.DateTimeField(blank=True, null=True)
	modified_by = models.CharField(max_length=45, blank=True, null=True)
	isDeleted = models.BooleanField(default = 0)

	def __str__(self):
		return '%s %s %s %s' % (self.student.user.username, self.leave_from, self.leave_to, self.reason)

	@property
	def isDelete(self):
		return bool(self.isDeleted())

class MessRefund(models.Model):
	# mess_leave = models.ForeignKey(MessLeave, models.DO_NOTHING, blank = True, null = True)
	student = models.ForeignKey(Student, models.DO_NOTHING, blank = True, null = True)
	account_number = models.CharField(max_length=18, blank = True, null = True)
	account_holder_name = models.CharField(max_length = 20, blank = True, null = True)
	ifsc_code = models.CharField(max_length = 11, blank = True, null = True)
	timestamp = models.DateTimeField(default = timezone.now())
	refund_amount = models.IntegerField()
	created_at = models.DateTimeField(blank=True, null=True)
	created_by = models.CharField(max_length=45, blank=True, null=True)
	modified_at = models.DateTimeField(blank=True, null=True)
	modified_by = models.CharField(max_length=45, blank=True, null=True)
	isDeleted = models.BooleanField(default = 0)

	def __str__(self):
		return "{}".format(self.student.student_first_name)

	@property
	def isDelete(self):
		return bool(self.isDeleted())

class MessItems(models.Model):
	item_name = models.CharField(max_length=45, blank=False, null=False, unique = True)
	cost = models.FloatField(blank=False, null=False)
	quantity = models.IntegerField()
	timestamp = models.DateTimeField(blank=True, null=True)
	isDeleted = models.BooleanField(default = 0)

	def __str__(self):
		return "{}".format(self.item_name)

	@property
	def isDelete(self):
		return bool(self.isDeleted())

class OrderHistoryMess(models.Model):
	student = models.ForeignKey('api_integration.Student', models.DO_NOTHING, blank=True, null=True)
	item = models.ForeignKey(MessItems, models.DO_NOTHING, blank=True, null=True)
	quantity = models.IntegerField(blank=True, null=True)
	timestamp = models.DateTimeField(default= timezone.now())
	created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
	created_by = models.CharField(max_length=45, blank=True, null=True)
	modified_at = models.DateTimeField(blank=True, null=True)
	modified_by = models.CharField(max_length=45, blank=True, null=True)
	isDeleted = models.BooleanField(default = 0)

	def __str__(self):
		return "{} {}".format(self.student.user.username, self.item.item_name)

	@property
	def isDelete(self):
		return bool(self.isDeleted())


class OrderListMess(models.Model):
	student = models.ForeignKey('api_integration.Student', models.DO_NOTHING, blank=True, null=True)
	item = models.ForeignKey(MessItems, models.DO_NOTHING, blank=True, null=True)
	quantity = models.IntegerField(blank=True, null=True)
	timestamp = models.DateTimeField(default = timezone.now())
	created_at = models.DateTimeField(blank=True, null=True)
	created_by = models.CharField(max_length=45, blank=True, null=True)
	modified_at = models.DateTimeField(blank=True, null=True)
	modified_by = models.CharField(max_length=45, blank=True, null=True)
	isDeleted = models.BooleanField(default = 0)

	def __str__(self):
		return "{}".format(self.student.user.username)

	@property
	def isDelete(self):
		return bool(self.isDeleted())


class MessFeedback(models.Model):
	student = models.ForeignKey('api_integration.Student', models.DO_NOTHING, blank=True, null=True)
	feedback = models.CharField(max_length=256, blank=True, null=True)
	room_no = models.IntegerField(blank=True, null=True)
	comp_img = models.ImageField(upload_to='images/'+str(datetime.now()),blank=True,null=True)
	timestamp = models.DateTimeField(default=timezone.now())
	created_at = models.DateTimeField(blank=True, null=True)
	created_by = models.CharField(max_length=45, blank=True, null=True)
	modified_at = models.DateTimeField(blank=True, null=True)
	modified_by = models.CharField(max_length=45, blank=True, null=True)
	isDeleted = models.BooleanField(default = 0)

	def __str__(self):
		return "{} {}".format(self.student.user.username, self.feedback)

	@property
	def isDelete(self):
		return bool(self.isDeleted())
