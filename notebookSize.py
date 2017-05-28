#!/usr/bin/env python
#coding:utf-8
# pepper는 1.4kg 미만의 노트북 모델을 타겟으로 한다.
MODELS = []

# 리스트의 순서 : 회사, 모델명, 가로mm, 세로mm, 높이mm, 무게kg
# 삼성
MODELS.append(["samsung", "NT500R4P-LD1S", 336.0, 230.5, 20.9, 1.65])
MODELS.append(["samsung", "NT900X3H-K38", 313.8, 218.5, 13.4, 0.86])
MODELS.append(["samsung", "NT900X3H-K38L", 318.8, 218.5, 13.4, 0.86])
MODELS.append(["samsung", "NT900X5J-K28S", 346.5, 226.8, 14.5, 1.29])
MODELS.append(["samsung", "NT900X5H-K24S", 346.5, 236.8, 14.5, 1.29])

# 레노버
MODELS.append(["lenovo", "X1-CARBON", 323.5, 217.1, 15.95, 1.13])
MODELS.append(["lenovo", "SlimBook110s", 292.0, 202.0, 17.8, 0.96])
MODELS.append(["lenovo", "IdeaPadMiix510 80XE006XKR", 300.0, 205.0, 9.9, 1.23])

# 애플
MODELS.append(["apple", "MacBook", 280.5, 196.5, 13.1, 0.92])
MODELS.append(["apple", "MacBookAir", 325.0, 227.0, 17.0, 1.35])
MODELS.append(["apple", "MacBookPro13", 304.1, 212.4, 14.9, 1.37])

def averageSize():
	"""
	각 모델의 평균사이즈를 구하는 함수이다.
	"""
	width = 0.0
	height = 0.0
	depth = 0.0
	total = 0

	for m in MODELS:
		if m[5] > 1.4: # pepper 프로젝트는 1.4킬로그램 미만의 노트북만 취급한다.
			continue
		width += m[2]
		height += m[3]
		depth += m[4]
		total += 1
	print("Average  Width : %.1f" % ( width / total))
	print("Average Height : %.1f" % ( height / total))
	print("Average  Depth : %.1f" % ( depth / total))

def main():
	averageSize()

if __name__ == "__main__":
	main()
