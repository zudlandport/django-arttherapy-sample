# Generated by Django 3.0.3 on 2020-02-24 17:33

from django.db import migrations

def forwards_func(apps, schema_editor):
   # We get the model from the versioned app registry;
   # if we directly import it, it'll be the wrong version

   db_alias = schema_editor.connection.alias

   ## PAINT COLOR LOOKUP TABLE POPULATE:
   paintcolor = apps.get_model("trackart", "paintcolor")
   paintcolor.objects.using(db_alias).bulk_create([
      paintcolor(paintcolortitle="Red"),
      paintcolor(paintcolortitle="Yellow"),
      paintcolor(paintcolortitle="Blue"),
      paintcolor(paintcolortitle="Orange"),
      paintcolor(paintcolortitle="Green"),
      paintcolor(paintcolortitle="Purple"),
      paintcolor(paintcolortitle="Gray"),
      paintcolor(paintcolortitle="Black"),
      paintcolor(paintcolortitle="White"),
   ])

   ## CLIENT MOOD LOOKUP TABLE POPULATE:
   clientmood = apps.get_model("trackart", "clientmood")
   clientmood.objects.using(db_alias).bulk_create([
      clientmood(clientmoodtitle="Happy"),
      clientmood(clientmoodtitle="Sad"),
      clientmood(clientmoodtitle="Angry"),
      clientmood(clientmoodtitle="Relaxed"),
      clientmood(clientmoodtitle="Annoyed"),
      clientmood(clientmoodtitle="Sleepy")
   ])


def reverse_func(apps, schema_editor):
   # forwards_func() creates two Country instances,
   # so reverse_func() should delete them.
   db_alias = schema_editor.connection.alias
   paintcolor = apps.get_model("trackart", "paintcolor")
   paintcolor.objects.using(db_alias).filter(paintcolortitle__in=["Red", "Yellow", "Blue", "Orange", "Green", "Purple", "Gray", "Black", "White"]).delete()
   clientmood = apps.get_model("trackart", "clientmood")
   clientmood.objects.using(db_alias).filter(clientmoodtitle__in=["Happy","Sad","Angry","Relaxed","Annoyed","Sleepy"]).delete()


class Migration(migrations.Migration):

	dependencies = [
		('trackart', '0001_initial'),
	]
	
	
	operations = [
		migrations.RunPython(forwards_func, reverse_func),
	]
	