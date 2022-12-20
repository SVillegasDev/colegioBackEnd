# Generated by Django 4.1 on 2022-12-20 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_profesor_user_alter_profesor_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profesor",
            name="user",
        ),
        migrations.AlterField(
            model_name="profesor",
            name="id",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="app.user",
            ),
        ),
    ]