congratulation_prize_sheet.cell("D{0}".format(excel_row_num)).\
    value = unicode(prize_rank_dict[rank_num]["name"])

# 당첨자 정보를 데이터스토어에 저장하기
winning_member = WinningEntity(winning_rank=rank_num,
    winning_name = unicode(temp_winning_person[0]),
    winning_email = unicode(temp_winning_person[1]),
    winning_product = unicode(prize_rank_dict[rank_num]["name"]))
winning_member.put()

# excel row number 증가시키기
excel_row_num += 1