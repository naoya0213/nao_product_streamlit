import streamlit as st
from PIL import Image
from portrait import portrait

f = st.file_uploader('Upload image file')
if (f):
    with open(f'static\modnet_image\input\\input.jpg', 'wb') as file:
        file.write(f.read())
    file.close()
    st.image(portrait('static\modnet_image\input\\input.jpg'))
# # 先頭４バイト（マジックナンバー）を取得
# b = f.read(4)

# # マジックナンバーが jpg だった場合
# if f and b == b'\xff\xd8\xff\xe0':
#     # ファイルを画像として表示（f.name でファイル名を取得）
#     st.image(f, caption=f.name, width=100)

#     # ファイルの内容を書き込み（元がバイトデータなので read で読み込み）
#     with open(f'new_{f.name}', 'wb') as file:
#         file.write(f.read())
# # image = Image.open(R'C:\Users\81907\Desktop\product\sample_images\smple.jpeg')

# st.image(image, caption='サンプル',use_column_width=True)