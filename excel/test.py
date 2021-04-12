import xlwt
import numpy as np 

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

def write_one_row(sheet, row, col_ind):
    for i in range(len(row)):
        sheet1.write(col_ind, i, row[i], set_style('Arial', 200))


if __name__ == '__main__':
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('caption', cell_overwrite_ok=True)
    row = ['图片名称', '标签', '生成语义', '语义相似性']
    for i in range(len(row)):
        sheet1.write(0, i, row[i], set_style('Arial', 200))

    image_name_list = np.load('image_name.npy', allow_pickle=True)
    label_list = np.load('label.npy', allow_pickle=True)
    caption_list = np.load('caption.npy', allow_pickle=True)
    bleu_list = np.load('bleu.npy', allow_pickle=True)

    col_ind = 1
    for image_name, label, caption, bleu in zip(image_name_list, label_list, caption_list, bleu_list):
        new_label = ''
        for l in label:
            new_label += l[:-1]
        row = [image_name, new_label, caption, bleu]
        # print(row)
        write_one_row(sheet1, row, col_ind)
        col_ind += 1

    f.save('1.xls')