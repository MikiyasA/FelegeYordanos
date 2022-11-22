# Generated by Django 4.1 on 2022-10-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membermgmt', '0012_alter_comment_type_alter_course_current_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='criticality',
            field=models.CharField(blank=True, choices=[('ማያስቸኩል', 'ማያስቸኩል'), ('መካከለኛ', 'መካከለኛ'), ('አስቸኩይ', 'አስቸኩይ')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='comment',
            name='type',
            field=models.CharField(choices=[('መጨመር ያለበት', 'መጨመር ያለበት'), ('መስተካከል ያለበት', 'መስተካከል ያለበት'), ('አስተያየት', 'አስተያየት'), ('መዳረሻ ገጽ ጭማሪ ጥያቄ', 'መዳረሻ ገጽ ጭማሪ ጥያቄ'), ('ማይሰራ ነገር', 'ማይሰራ ነገር')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='current_class',
            field=models.CharField(choices=[('ቀዳማይ', 'ቀዳማይ'), ('ካልዓይ', 'ካልዓይ'), ('ራብዓይ', 'ራብዓይ'), ('ሣልሣይ', 'ሣልሣይ')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fekad',
            name='approval',
            field=models.CharField(choices=[('ጸድቁአል', 'ጸድቁአል'), ('አልጸደቀም', 'አልጸደቀም'), ('ተጠይቁአል', 'ተጠይቁአል')], default='ተጠይቁአል', max_length=50),
        ),
        migrations.AlterField(
            model_name='fekad',
            name='kifl',
            field=models.CharField(blank=True, choices=[('የሰንበት ት/ቤቱ ቁጥጥርና ክትትል', 'የሰንበት ት/ቤቱ ቁጥጥርና ክትትል'), ('ሕጻናት ክፍል', 'ሕጻናት ክፍል'), ('ንብረት አስተዳደርና ግዢ ዘርፍ', 'ንብረት አስተዳደርና ግዢ ዘርፍ'), ('የሰንበት ት/ቤቱ ስራ አመራር ጉባኤ አባል', 'የሰንበት ት/ቤቱ ስራ አመራር ጉባኤ አባል'), ('ልማት፤ሙያ እና በጎ አድራጎት ክፍል', 'ልማት፤ሙያ እና በጎ አድራጎት ክፍል'), ('ትምሕርት ክፍል', 'ትምሕርት ክፍል'), ('የሰንበት ት/ቤቱ ጸሃፊ', 'የሰንበት ት/ቤቱ ጸሃፊ'), ('መዝሙር ጣእመ ዜማ ክፍል', 'መዝሙር ጣእመ ዜማ ክፍል'), ('የአባላት ክብካቤና ግንኙነት ክፍል', 'የአባላት ክብካቤና ግንኙነት ክፍል'), ('መረጃ ጥበብና መዛግብት ድምጸ ወምስል ክፍል', 'መረጃ ጥበብና መዛግብት ድምጸ ወምስል ክፍል'), ('የሰንበት ት/ቤቱ ዋና ሰብሳቢ', 'የሰንበት ት/ቤቱ ዋና ሰብሳቢ'), ('የሒሳብ አስተዳደር ዘርፍ', 'የሒሳብ አስተዳደር ዘርፍ'), ('ስነ-ጥበብ ክፍል', 'ስነ-ጥበብ ክፍል'), ('የሕዝብ ግንኙነት ዘርፍ', 'የሕዝብ ግንኙነት ዘርፍ'), ('የጥናትና ምርምር ዘርፍ', 'የጥናትና ምርምር ዘርፍ'), ('የዕቅድ ዝግጅት አፈጻጸምና ፕሮጀክት ዘርፍ', 'የዕቅድ ዝግጅት አፈጻጸምና ፕሮጀክት ዘርፍ'), ('የመረጃ አደረጃጀትና ትንተና ዘርፍ', 'የመረጃ አደረጃጀትና ትንተና ዘርፍ')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='activity',
            field=models.CharField(choices=[('አያገለግሉም', 'አያገለግሉም'), ('ያገለግላሉ', 'ያገለግላሉ')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='dikuna',
            field=models.CharField(blank=True, choices=[('-ዲያቆን', '-ዲያቆን'), ('እጩ ዲያቆን', 'እጩ ዲያቆን'), ('እጩ ቀሲስ', 'እጩ ቀሲስ'), ('-ቀሲስ', '-ቀሲስ')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='kifl',
            field=models.CharField(blank=True, choices=[('የሰንበት ት/ቤቱ ቁጥጥርና ክትትል', 'የሰንበት ት/ቤቱ ቁጥጥርና ክትትል'), ('ሕጻናት ክፍል', 'ሕጻናት ክፍል'), ('ንብረት አስተዳደርና ግዢ ዘርፍ', 'ንብረት አስተዳደርና ግዢ ዘርፍ'), ('የሰንበት ት/ቤቱ ስራ አመራር ጉባኤ አባል', 'የሰንበት ት/ቤቱ ስራ አመራር ጉባኤ አባል'), ('ልማት፤ሙያ እና በጎ አድራጎት ክፍል', 'ልማት፤ሙያ እና በጎ አድራጎት ክፍል'), ('ትምሕርት ክፍል', 'ትምሕርት ክፍል'), ('የሰንበት ት/ቤቱ ጸሃፊ', 'የሰንበት ት/ቤቱ ጸሃፊ'), ('መዝሙር ጣእመ ዜማ ክፍል', 'መዝሙር ጣእመ ዜማ ክፍል'), ('የአባላት ክብካቤና ግንኙነት ክፍል', 'የአባላት ክብካቤና ግንኙነት ክፍል'), ('መረጃ ጥበብና መዛግብት ድምጸ ወምስል ክፍል', 'መረጃ ጥበብና መዛግብት ድምጸ ወምስል ክፍል'), ('የሰንበት ት/ቤቱ ዋና ሰብሳቢ', 'የሰንበት ት/ቤቱ ዋና ሰብሳቢ'), ('የሒሳብ አስተዳደር ዘርፍ', 'የሒሳብ አስተዳደር ዘርፍ'), ('ስነ-ጥበብ ክፍል', 'ስነ-ጥበብ ክፍል'), ('የሕዝብ ግንኙነት ዘርፍ', 'የሕዝብ ግንኙነት ዘርፍ'), ('የጥናትና ምርምር ዘርፍ', 'የጥናትና ምርምር ዘርፍ'), ('የዕቅድ ዝግጅት አፈጻጸምና ፕሮጀክት ዘርፍ', 'የዕቅድ ዝግጅት አፈጻጸምና ፕሮጀክት ዘርፍ'), ('የመረጃ አደረጃጀትና ትንተና ዘርፍ', 'የመረጃ አደረጃጀትና ትንተና ዘርፍ')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='category',
            field=models.CharField(blank=True, choices=[('ንዋየ ቅድሳት', 'ንዋየ ቅድሳት'), ('የኤሌክትሮኒክስ የአይቲ እቃዎች', 'የኤሌክትሮኒክስ/የአይቲ እቃዎች'), ('ምግብ ነክ ቁሶች', 'ምግብ ነክ ቁሶች'), ('የድግስ እቃዎች', 'የድግስ እቃዎች'), ('የጽህፈት መሳሪያቆች', 'የጽህፈት መሳሪያቆች'), ('የቢሮ እቃዎች', 'የቢሮ እቃዎች')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='condition',
            field=models.CharField(choices=[('አዲስ', 'አዲስ'), ('የሚወገድ', 'የሚወገድ'), ('ያገለገለ', 'ያገለገለ'), ('አሮጌ', 'አሮጌ')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(blank=True, choices=[('ቆሚ', 'ቆሚ'), ('አላቂ', 'አላቂ')], max_length=100, null=True),
        ),
    ]