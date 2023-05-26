# Generated by Django 4.2 on 2023-05-16 03:48

import baykeshop.tinymce
from django.conf import settings
import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaykeMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='分类名称')),
                ('icon', models.CharField(blank=True, default='', max_length=50, verbose_name='分类图标')),
                ('desc', models.CharField(blank=True, default='', max_length=150, verbose_name='描述')),
                ('keywords', models.CharField(blank=True, default='', max_length=150, verbose_name='关键字')),
                ('sort', models.PositiveSmallIntegerField(default=1, verbose_name='排序')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': '菜单',
                'verbose_name_plural': '菜单',
                'ordering': ['-sort'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('order_sn', models.CharField(blank=True, default='', editable=False, help_text='订单号', max_length=32, unique=True, verbose_name='订单号')),
                ('trade_sn', models.CharField(blank=True, editable=False, help_text='交易号', max_length=64, null=True, unique=True, verbose_name='交易号')),
                ('pay_status', models.IntegerField(choices=[(1, '待支付'), (2, '待发货'), (3, '待收货'), (4, '待评价'), (5, '已完成'), (6, '已取消')], default=1, editable=False, help_text='支付状态', verbose_name='支付状态')),
                ('pay_method', models.IntegerField(blank=True, choices=[(1, '货到付款'), (2, '支付宝'), (3, '微信支付'), (4, '余额支付')], editable=False, help_text='支付方式', null=True, verbose_name='支付方式')),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, verbose_name='商品总金额')),
                ('order_mark', models.CharField(blank=True, default='', help_text='订单备注', max_length=100, verbose_name='订单备注')),
                ('name', models.CharField(max_length=50, verbose_name='签收人')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('email', models.EmailField(blank=True, default='', max_length=50, verbose_name='邮箱')),
                ('address', models.CharField(max_length=200, verbose_name='地址')),
                ('pay_time', models.DateTimeField(blank=True, editable=False, help_text='支付时间', null=True, verbose_name='支付时间')),
                ('owner', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'BaykeOrder',
                'verbose_name_plural': 'BaykeOrders',
                'ordering': ['-add_date'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='分类名称')),
                ('icon', models.CharField(blank=True, default='', max_length=50, verbose_name='分类图标')),
                ('desc', models.CharField(blank=True, default='', max_length=150, verbose_name='描述')),
                ('keywords', models.CharField(blank=True, default='', max_length=150, verbose_name='关键字')),
                ('pic', models.ImageField(blank=True, default='default/cate.png', max_length=200, upload_to='product/cate/', verbose_name='推荐图')),
                ('is_nav', models.BooleanField(default=True, verbose_name='菜单推荐')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baykeshop.baykeproductcategory', verbose_name='父级')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'BaykeProductCategory',
                'verbose_name_plural': 'BaykeProductCategorys',
                'ordering': ['-add_date'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeProductSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='规格名')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'BaykeProductSpec',
                'verbose_name_plural': 'BaykeProductSpecs',
                'ordering': ['-add_date'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeVerifyCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('code', models.CharField(blank=True, default='', max_length=4, verbose_name='验证码')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'VerifyCode',
                'verbose_name_plural': 'VerifyCodes',
                'ordering': ['-add_date'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeUserBalanceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='金额')),
                ('change_status', models.PositiveSmallIntegerField(blank=True, choices=[(1, '增加'), (2, '支出')], null=True)),
                ('change_way', models.PositiveSmallIntegerField(choices=[(1, '线上充值'), (2, '管理员手动更改'), (3, '余额抵扣商品')], default=2)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': '余额明细',
                'verbose_name_plural': '余额明细',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='手机号')),
                ('email', models.EmailField(blank=True, editable=False, max_length=254, null=True, unique=True, verbose_name='邮箱')),
                ('avatar', models.ImageField(blank=True, default='avatar/default.png', max_length=200, upload_to='avatar/', verbose_name='头像')),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, verbose_name='余额')),
                ('desc', models.CharField(blank=True, default='', max_length=150, verbose_name='描述')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'BaykeUser',
                'verbose_name_plural': 'BaykeUsers',
                'ordering': ['-add_date'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('img', models.ImageField(max_length=200, upload_to='upload/editor/')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': '富文本编辑器图片上传',
                'verbose_name_plural': '富文本编辑器图片上传',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('site_name', models.CharField(blank=True, default='Bayke', max_length=50, verbose_name='站点名称')),
                ('site_title', models.CharField(blank=True, default='Bayke商城管理系统', max_length=50, verbose_name='站点标题')),
                ('site_header', models.CharField(blank=True, default='Bayke System', max_length=50, verbose_name='站点描述')),
                ('beian', models.CharField(blank=True, default='', max_length=200, verbose_name='备案信息')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'BaykeSite',
                'verbose_name_plural': 'BaykeSites',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeProductSPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('desc', models.CharField(blank=True, default='', max_length=150, verbose_name='描述')),
                ('keywords', models.CharField(blank=True, default='', max_length=150, verbose_name='关键字')),
                ('content', baykeshop.tinymce.TinymceField(tinymce={'automatic_uploads': True, 'browser_spellcheck': True, 'contextmenu': False, 'file_picker_types': 'file image media', 'image_title': False, 'images_file_types': 'jpg,svg,webp,png,gif', 'images_reuse_filename': True, 'images_upload_url': '/upload/tinymce/', 'plugins': ['advlist', 'autolink', 'link', 'image', 'lists', 'charmap', 'preview', 'anchor', 'pagebreak', 'searchreplace', 'wordcount', 'visualblocks', 'visualchars', 'code', 'fullscreen', 'insertdatetime', 'media', 'table', 'emoticons', 'template', 'help'], 'toolbar': 'undo redo | styles | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | print preview media | forecolor backcolor emoticons'}, verbose_name='详情')),
                ('after_sale', models.TextField(blank=True, default='', verbose_name='售后服务')),
                ('pic', models.ImageField(max_length=200, upload_to='goods/%Y/', verbose_name='主图')),
                ('freight', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, verbose_name='运费')),
                ('cates', models.ManyToManyField(to='baykeshop.baykeproductcategory', verbose_name='商品分类')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'BaykeSpu',
                'verbose_name_plural': 'BaykeSpus',
                'ordering': ['-add_date'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeProductSpecOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='规格值')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baykeshop.baykeproductspec', verbose_name='规格')),
            ],
            options={
                'verbose_name': 'BaykeProductSpecOption',
                'verbose_name_plural': 'BaykeProductSpecOptions',
                'ordering': ['-add_date'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeProductSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('pic', models.ImageField(max_length=200, upload_to='product/%Y/', verbose_name='主图')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='售价')),
                ('cost_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='原价')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='库存')),
                ('sales', models.PositiveIntegerField(default=0, editable=False, verbose_name='销量')),
                ('item_id', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='商品编号')),
                ('weight', models.PositiveSmallIntegerField(default=0, help_text='单位：千克', verbose_name='重量')),
                ('volume', models.PositiveSmallIntegerField(default=0, help_text='单位：立方米', verbose_name='体积')),
                ('is_release', models.BooleanField(default=True, verbose_name='上架')),
                ('options', models.ManyToManyField(blank=True, to='baykeshop.baykeproductspecoption', verbose_name='规格值')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
                ('spu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baykeshop.baykeproductspu', verbose_name='商品')),
            ],
            options={
                'verbose_name': 'BaykeProductSKU',
                'verbose_name_plural': 'BaykeProductSKUs',
                'ordering': ['price'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeProductBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('img', models.ImageField(max_length=200, upload_to='upload/', verbose_name='图片')),
                ('desc', models.CharField(blank=True, default='', max_length=150, verbose_name='图片说明')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
                ('spu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baykeshop.baykeproductspu', verbose_name='商品')),
            ],
            options={
                'verbose_name': 'BaykeProductBanner',
                'verbose_name_plural': 'BaykeProductBanners',
                'ordering': ['-add_date'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='分类名称')),
                ('icon', models.CharField(blank=True, default='', max_length=50, verbose_name='分类图标')),
                ('desc', models.CharField(blank=True, default='', max_length=150, verbose_name='描述')),
                ('keywords', models.CharField(blank=True, default='', max_length=150, verbose_name='关键字')),
                ('sort', models.PositiveSmallIntegerField(default=1, verbose_name='排序')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('menus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baykeshop.baykemenu', verbose_name='菜单')),
                ('permission', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.permission', verbose_name='权限')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': '菜单权限',
                'verbose_name_plural': '菜单权限',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeOrderSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('title', models.CharField(editable=False, max_length=100, verbose_name='商品标题')),
                ('options', models.JSONField(editable=False, verbose_name='商品规格')),
                ('price', models.DecimalField(decimal_places=2, editable=False, max_digits=8, verbose_name='商品单价')),
                ('content', models.TextField(editable=False, verbose_name='商品详情')),
                ('count', models.IntegerField(default=1, verbose_name='数量')),
                ('is_commented', models.BooleanField(default=False, verbose_name='是否已评价')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baykeshop.baykeorder', verbose_name='订单')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
                ('sku', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baykeshop.baykeproductsku')),
            ],
            options={
                'verbose_name': 'BaykeOrderSKU',
                'verbose_name_plural': 'BaykeOrderSKUs',
                'ordering': ['-add_date'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeOrderComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('tag', models.CharField(blank=True, max_length=80, null=True, unique=True, verbose_name='标记')),
                ('content', models.CharField(max_length=200, verbose_name='留言内容')),
                ('comment_choices', models.PositiveSmallIntegerField(choices=[(5, '好评'), (3, '中评'), (1, '差评')], default=5, verbose_name='评分')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': '商品评价',
                'verbose_name_plural': '商品评价',
                'ordering': ['-add_date'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('count', models.PositiveIntegerField(default=1, verbose_name='数量')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baykeshop.baykeproductsku', verbose_name='规格商品')),
            ],
            options={
                'verbose_name': 'BaykeCart',
                'verbose_name_plural': 'BaykeCarts',
                'ordering': ['-add_date'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('img', models.ImageField(max_length=200, upload_to='upload/', verbose_name='图片')),
                ('desc', models.CharField(blank=True, default='', max_length=150, verbose_name='图片说明')),
                ('place', models.CharField(blank=True, help_text='留空则为首页banner，否则为指定位置banner', max_length=50, null=True, unique=True, verbose_name='位置标识')),
                ('target_url', models.CharField(blank=True, default='', max_length=150, verbose_name='跳转地址')),
                ('sort', models.PositiveSmallIntegerField(default=1, verbose_name='排序')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'ordering': ['sort'],
                'abstract': False,
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeArticleTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='标签名')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'BaykeArticleTag',
                'verbose_name_plural': 'BaykeArticleTags',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='分类名称')),
                ('icon', models.CharField(blank=True, default='', max_length=50, verbose_name='分类图标')),
                ('desc', models.CharField(blank=True, default='', max_length=150, verbose_name='描述')),
                ('keywords', models.CharField(blank=True, default='', max_length=150, verbose_name='关键字')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'BaykeArticleCategory',
                'verbose_name_plural': 'BaykeArticleCategorys',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('desc', models.CharField(blank=True, default='', max_length=150, verbose_name='描述')),
                ('keywords', models.CharField(blank=True, default='', max_length=150, verbose_name='关键字')),
                ('content', baykeshop.tinymce.TinymceField(tinymce={'automatic_uploads': True, 'browser_spellcheck': True, 'contextmenu': False, 'file_picker_types': 'file image media', 'image_title': False, 'images_file_types': 'jpg,svg,webp,png,gif', 'images_reuse_filename': True, 'images_upload_url': '/upload/tinymce/', 'plugins': ['advlist', 'autolink', 'link', 'image', 'lists', 'charmap', 'preview', 'anchor', 'pagebreak', 'searchreplace', 'wordcount', 'visualblocks', 'visualchars', 'code', 'fullscreen', 'insertdatetime', 'media', 'table', 'emoticons', 'template', 'help'], 'toolbar': 'undo redo | styles | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | print preview media | forecolor backcolor emoticons'}, verbose_name='详情')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baykeshop.baykearticlecategory', verbose_name='文章分类')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
                ('tags', models.ManyToManyField(blank=True, to='baykeshop.baykearticletag', verbose_name='标签')),
            ],
            options={
                'verbose_name': 'BaykeArticle',
                'verbose_name_plural': 'BaykeArticles',
                'ordering': ['-add_date'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='BaykeAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='签收人')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('email', models.EmailField(blank=True, default='', max_length=50, verbose_name='邮箱')),
                ('province', models.CharField(max_length=150, verbose_name='省')),
                ('city', models.CharField(max_length=150, verbose_name='市')),
                ('county', models.CharField(max_length=150, verbose_name='区/县')),
                ('address', models.CharField(max_length=150, verbose_name='详细地址')),
                ('is_default', models.BooleanField(default=False, verbose_name='设为默认')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('site', models.ForeignKey(blank=True, editable=False, help_text='关联站点，如果选择，该信息仅在指定站点显示', null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': '收货地址',
                'verbose_name_plural': '收货地址',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='baykecart',
            constraint=models.UniqueConstraint(fields=('owner', 'sku'), name='unique_owner_sku'),
        ),
    ]