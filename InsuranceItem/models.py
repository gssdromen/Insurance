from django.db import models

# Create your models here.
class InsuranceItem(models.Model):
    apply_num = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=30)
    dealer_name = models.CharField(max_length=80)
    payback_status = models.TextField()
    from_where = models.CharField(max_length=30)
    is_overdue = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    is_clean = models.BooleanField(default=False)
    apply_date = models.DateField(auto_now=False, auto_now_add=True)
    update_date = models.DateField(auto_now=True, auto_now_add=True)
    last_status = models.TextField()
    watching_flag = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s:%s' % (self.apply_num, self.name)
