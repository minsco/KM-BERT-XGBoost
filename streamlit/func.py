import torch
from transformers import BertForSequenceClassification, BertTokenizer

model = BertForSequenceClassification.from_pretrained("madatnlp/km-bert", num_labels=17)
model.load_state_dict(torch.load("best_model.pt", map_location=torch.device('cpu')), strict=False)
tokenizer = BertTokenizer.from_pretrained("madatnlp/km-bert")
model.eval()

mapping = {
    0: '일반의', 1: '내과', 2: '신경과', 3: '정신과', 4: '외과', 5: '정형외과', 6: '신경외과',
    7: '흉부외과', 8: '성형외과', 9: '마취통증의학과', 10: '산부인과', 11: '소아청소년과',
    12: '안과', 13: '이비인후과', 14: '피부과', 15: '비뇨기과', 16: '영상의학과',
    17: '방사선 종양학과', 18: '병리과', 19: '진단검사의학과', 20: '결핵과',
    21: '재활의학과', 22: '핵의학과', 23: '가정의학과', 24: '응급의학과',
    25: '산업의학과', 26: '예방의학과', 50: '구강악안면외과', 51: '치과보철과',
    52: '치과교정과', 53: '소아치과', 54: '치주과', 55: '치과보존과',
    56: '구강내과', 57: '구강악안면방사선과', 58: '구강병리과',
    59: '예방치과', 80: '한방내과', 81: '한방부인과',
    82: '한방소아과', 83: '한방안·이비인후·피부 과',
    84: '한방신경정신 과', 85: '침구 과',
    86: '한방재활의학 과',87:'사상체질 과',
    88: '한방응급 과', None: "Nan"
}

pain_list = ['팔', '다리', '머리', '심장', '몸통']

def get_age_group(n):
    n = int(n)
    if n >= 85:
        group = 18
    else:
        group = (n // 5) + 1
    return group