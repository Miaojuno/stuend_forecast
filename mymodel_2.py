import csv
import pandas as pd
import numpy as np
from keras.layers import Dense, Conv1D, LocallyConnected1D
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.models import Sequential

# 标签
# 0:id 1:flag 2:teacher_level 3:teacher_num 4:homework_dif 5:homework_num
# 6:student_level 7:student_num 8:student_current_level 9:student_current_num
# 10:qst_dif 11:qst_num 12:point_dif 13:point_num 14:stu_point_level 15:stu_point_num

# 源数据行数：16522796 + 1 = 16522797
class bp_model():
    def __init__(self,raw_data_path,model_path):
        self.raw_data_path=raw_data_path
        self.model_path=model_path

        self.bp_main()
    def bp_main(self):
        model = Sequential()


        # model.add(Dropout(0.2))
        # model.add(LocallyConnected1D(filters=128, kernel_size=2, strides=2, activation='relu' , batch_input_shape=(0,10,1) ))
        # model.add(Dense(32 , activation='relu' ))
        model.add(Dense(5, activation='relu',input_dim=10))
        model.add(Dense(1, activation='sigmoid' ))
        adam = Adam(lr=0.005, beta_1=0.9, beta_2=0.999, epsilon=1e-08, amsgrad=True)
        model.compile(loss="binary_crossentropy", optimizer=adam, metrics=["accuracy"])
        model.fit_generator(generator=self.get_train_batch(), steps_per_epoch=int(16522797*0.9/5000),
                            validation_data=self.get_test_batch(), validation_steps=int(16522797*0.1/5000),
                            epochs=3, verbose=1,shuffle=1)
        model.save(self.model_path)



    # 获取训练集（迭代器）
    def get_train_batch(self):
        for i,it in enumerate(self.get_x_y()):
            x=it[0]
            y=it[1]
            x_train, x_test, y_train, y_test = \
                train_test_split(x, y, test_size=0.1, random_state=0)  # 分割数据集
            x=np.array(x_train)
            y=np.array(y_train)
            # print(x.shape)
            # print(y.shape)
            yield (x,y)

    # 获取测试集（迭代器）
    def get_test_batch(self):
        for i,it in enumerate(self.get_x_y()):
            x=it[0]
            y=it[1]
            x_train, x_test, y_train, y_test = \
                train_test_split(x, y, test_size=0.1, random_state=0)  # 分割数据集
            x = np.array(x_train)
            y = np.array(y_train)
            yield (x, y)

    # 获取数据集（迭代器）
    def get_x_y(self):
        max3 = 183803; min3 = 1; max5 = 7395; min5 = 1
        max7 = 3357; min7 = 1; max9 = 1846; min9 = 1
        max11 = 15114; min11 = 1
        maxlist=[max3,max5,max7,max9,max11]
        reader = pd.read_csv(self.raw_data_path, iterator=True,header=None)
        while 1:
            try:
                df = reader.get_chunk(5000)
                # df=df.values.tolist()
                x=df.iloc[:,[2,4,6,8,10,11,12,14,15]].values.tolist()
                y=df.iloc[:,1].values.tolist()

                # y     ->    1=true 0=false
                y0=[]
                for it in y:
                    if it==1:
                        y0.append(1)
                    else:
                        y0.append(0)

                # x0=[]
                # for it in x:
                #     sx=[]
                #     for i,num in enumerate(it):
                #         if i%2==0:
                #             nx=num
                #         else:
                #             maxnum = maxlist[round((i - 1) / 2)]
                #             if num > 0.5 * maxnum:
                #                 ratio = 1
                #             elif num > 0.1 * maxnum:
                #                 ratio = 0.9
                #             else:
                #                 ratio = (num - 1) / (0.1 * maxnum - 1) * 0.9
                #             nx = 0.5 + (nx - 0.5) * ratio
                #         sx.append(nx)
                #     x0.append(sx)

                yield (x,y0)
            except StopIteration:
                reader.close()
                reader = pd.read_csv(self.raw_data_path, iterator=True,header=None)

bp_model(raw_data_path=r'F:\Date\student\raw_data_bp2.csv'
         , model_path='F:\Date\student\model_10.h5')