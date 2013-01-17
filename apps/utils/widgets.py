# -*- coding: utf-8 -*-
from django import forms
import os
from django.utils.safestring import mark_safe
import settings

class Redactor(forms.Textarea):
    toolbar = u'default' #'mini'
    class Media:
        js = (
            '/media/js/jquery.js',
            '/media/js/redactor/redactor.js',
            )
        css = {
            'all': ('/media/js/redactor/css/redactor.css',)
        }

    def __init__(self, attrs=None):
        self.attrs = attrs
        if attrs:
            self.attrs.update(attrs)
        super(Redactor,self).__init__(attrs)

    def render(self,name,value,attrs=None):
        rendered = super(Redactor,self).render(name, value, attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
        $(document).ready(
            function()
            {
                $('#id_%s').redactor({
                    focus: true,
                    toolbar:'%s',
                    imageUpload:'/upload_img/',
                    fileUpload:'/upload_file/',
                    lang:'ru'
                });
            }
        );
        </script>''' % (name,self.toolbar))

class MapCity(forms.TextInput):
    class Media:
        js = (
            '/media/js/jquery.js',
            'http://api-maps.yandex.ru/2.0-stable/?load=package.standard&lang=ru-RU&coordorder=longlat',
            )

    def __init__(self, attrs=None):
        self.attrs = attrs
        if attrs:
            self.attrs.update(attrs)
        super(MapCity,self).__init__(attrs)

    def render(self,name,value,attrs=None):
        rendered = super(MapCity,self).render(name, value, attrs)
        return rendered + mark_safe(u'''
        <div id="map" style="width: 600px; height: 400px"></div>
        <script type="text/javascript">
        $(function(){
            var coord_container = $('#id_coordinates_center');
            zoom_container = $('#id_zoom');
            var coords = coord_container.attr('value').split(',');
            var zoom = zoom_container.attr('value');
            var myMap;
            ymaps.ready(init);

            function init(){     
                myMap = new ymaps.Map ("map", {
                    center: [coords[0],coords[1]],
                    zoom: zoom,
                });
                myMap.controls.add(
                    new ymaps.control.ZoomControl()
                );
                myMap.controls.add(
                    new ymaps.control.SearchControl()
                );
                var placemark = new ymaps.Placemark(
                    [coords[0],coords[1]],{},{draggable: true}
                );
                myMap.geoObjects.add(placemark);
                myMap.geoObjects.events.add("dragend",function(e) {
                    coord_container.attr('value',placemark.geometry.getCoordinates());
                });
                myMap.events.add("click",function(e) {
                    var coords = e.get('coordPosition');
                    placemark.geometry.setCoordinates(coords);
                    coord_container.attr('value',placemark.geometry.getCoordinates());
                });
            }
        });
        </script>
        ''')

class MapObject(forms.TextInput):
    class Media:
        js = (
            '/media/js/jquery.js',
            'http://api-maps.yandex.ru/2.0-stable/?load=package.standard&lang=ru-RU&coordorder=longlat',
            )

    def __init__(self, attrs=None):
        self.attrs = attrs
        if attrs:
            self.attrs.update(attrs)
        super(MapObject,self).__init__(attrs)

    def render(self,name,value,attrs=None):
        rendered = super(MapObject,self).render(name, value, attrs)
        return rendered + mark_safe(u'''
        <div id="map" style="width: 600px; height: 400px"></div>
        <script type="text/javascript">
        $(function(){
            var coord_container = $('#id_coordinates');
            var coords = coord_container.attr('value').split(',');
            var zoom = 12;
            var myMap;
            ymaps.ready(init);

            function init(){     
                myMap = new ymaps.Map ("map", {
                    center: [coords[0],coords[1]],
                    zoom: zoom,
                });
                myMap.controls.add(
                    new ymaps.control.ZoomControl()
                );
                myMap.controls.add(
                    new ymaps.control.SearchControl()
                );
                var placemark = new ymaps.Placemark(
                    [coords[0],coords[1]],{},{draggable: true}
                );
                myMap.geoObjects.add(placemark);
                myMap.geoObjects.events.add("dragend",function(e) {
                    coord_container.attr('value',placemark.geometry.getCoordinates());
                });
                myMap.events.add("click",function(e) {
                    var coords = e.get('coordPosition');
                    placemark.geometry.setCoordinates(coords);
                    coord_container.attr('value',placemark.geometry.getCoordinates());
                });
            }
        });
        </script>
        ''')

class RedactorMini(Redactor):
    toolbar = u'mini'

class RedactorClassic(Redactor):
    toolbar = u'classic'


#class RedactorMicro(Redactor):
#    toolbar = u'micro'

class ColorPicker(forms.TextInput): # используется так же как редактор
    class Media:
        js = (
            '/media/js/jquery.js',
            '/media/js/color_picker/jquery.miniColors.js',
            )
        css = {
            'all': ('/media/js/color_picker/jquery.miniColors.css',)
        }

    def render(self,name,value,attrs=None):
        attrs = {'class':'color-picker', 'size':"6"}
        rendered = super(ColorPicker,self).render(name, value, attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
            $(document).ready( function() {
                $(".color-picker").miniColors({
                    letterCase: 'uppercase',
                    change: function(hex, rgb) {
                        logData('change', hex, rgb);
                    },
                    open: function(hex, rgb) {
                        logData('open', hex, rgb);
                    },
                    close: function(hex, rgb) {
                        logData('close', hex, rgb);
                    }
                });
            });
        </script>''')

class AdminImageCrop(forms.FileInput):
    path = ''
    img_width = 200

    def get_url(self, value):
        return u'<br><a href="/admin/crop/%s/%s/">Изменить миниатюру</a>' \
                % (self.path, value.instance.id)

    def get_img(self, url):
        file, ext = os.path.splitext(url)
        file = u'%s_crop.jpg' % file
        if os.path.isfile( settings.ROOT_PATH +file):
            url_img = file
        else:
            url_img = url
        return u'<img src="%s" style="width: %spx;" />' % (url_img, self.img_width)

    def render(self, name, value, attrs=None):
        if 'path' in self.attrs:
            self.path = self.attrs['path']
        if 'img_width' in self.attrs:
            self.img_width = self.attrs['img_width']
        output = []
        if value and hasattr(value, "url"):
            output.append((u'<a target="_blank" href="%s">%s</a>%s' % (value.url, self.get_img(value.url), self.get_url(value))))
        output.append(super(AdminImageCrop, self).render(name, value, attrs))
        return mark_safe(u''.join(output))

class AdminImageWidget(forms.FileInput):
    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            output.append((u'<a target="_blank" href="%s">'
                           u'<img src="%s" style="height: 100px;" /></a>'
                           u'<a href="/admin/crop/%s/?next=/admin/members/members/%s/">Изменить миниатюру</a>'
                           % (value.url, value.url, value.instance.id, value.instance.id)))
        output.append(super(AdminImageWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))