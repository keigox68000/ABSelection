def can_form_s(s):
    # 逆から検証するために、操作対象の文字列を逆にする
    s = s[::-1]
    # 操作できる文字列も逆にしておく
    operations = ["maerd", "remaerd", "esare", "resare"]    
    while s:
        # 現在の文字列の末尾が操作のいずれかに一致するかどうかを確認
        matched = False
        for op in operations:
            if s.startswith(op):
                # 一致する場合、その分だけ文字列を削除
                s = s[len(op):]
                matched = True
                break
        # いずれの操作にも一致しない場合、S=Tを満たすことは不可能
        if not matched:
            return False
    # 全ての操作が完了して文字列が空になれば、条件を満たす
    return True
# 入力
S = input()
# 判定
if can_form_s(S):
    print("YES")
else:
    print("NO")