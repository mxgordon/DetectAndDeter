from android.os import Bundle
from androidx.appcompat.app import AppCompatActivity
from com.example.detectanddeter import R
from java import jvoid, Override, static_proxy
from os import listdir

from ai import predict_text


class MainActivity(static_proxy(AppCompatActivity)):

    @Override(jvoid, [Bundle])
    def onCreate(self, state):
        AppCompatActivity.onCreate(self, state)
        self.setContentView(R.layout.activity_main)
        print(listdir())
        print(predict_text("hello"))