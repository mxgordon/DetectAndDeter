# from android.os import Bundle
# from androidx.appcompat.app import AppCompatActivity
# from com.example.detectanddeter import R
# from java import jvoid, Override, static_proxy
# from os import listdir
#
# from ai import AI
#
#
# class MainActivity(static_proxy(AppCompatActivity)):
#
#     @Override(jvoid, [Bundle])
#     def onCreate(self, state):
#         AppCompatActivity.onCreate(self, state)
#         print(listdir())
#         self.setContentView(R.layout.activity_main)
#         # print(listdir())
#         raise RuntimeError(type(R.raw.finalv1))
#         model = AI.load_learner(R.raw.finalv1)
#         print(model.predict_text("hello"))