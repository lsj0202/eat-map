from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Restaurant:
    def __init__(self, name, address, phone, category, description, latitude, longitude):
        self.name = name
        self.address = address
        self.phone = phone
        self.category = category
        self.description = description
        self.latitude = latitude
        self.longitude = longitude

# Sample restaurant data
restaurants = [
    Restaurant("선일", "서울특별시 영등포구 도림로64가길 2 (대림동)", "02-832-8900", "식육판매업", "우리동네 모범정육점", 37.4964300, 126.905171),
    Restaurant("충남정육점", "서울특별시 중구 퇴계로85길 27, 1층(황학동)", None, "식육판매업", "우리동네 모범정육점", 37.5669887, 127.019493),
    Restaurant("청구일등축산", "서울특별시 중구 다산로 184, 1층(신당동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5597005, 127.013685),
    Restaurant("푸른목장", "서울특별시 동작구 상도로 102, 성대시장 1층 (상도동)", "02-822-6310", "식육판매업", "우리동네 모범정육점", 37.4998546, 126.932025),
    Restaurant("금천외양간", "서울특별시 금천구 독산로204", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4654693, 126.902487),
    Restaurant("박서방네", "서울특별시 강동구 풍성로 54길 27, 1층 (성내동)", "02-485-4945", "식육즉석판매가공업", "우리동네 모범정육점", 37.5282455, 127.133566),
    Restaurant("㈜아울렛마트", "서울특별시 금천구 독산로40길 29", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4605889, 126.906189),
    Restaurant("싱싱정육점", "서울특별시 강서구 양천로28길 29, 상가동 1층(방화동, 방화2차우림루미아트아파트)", "02-2663-8028", "식육즉석판매가공업", "우리동네 모범정육점", 37.5717992, 126.821308),
    Restaurant("고기샵정육점", "서울특별시 양천구 은행정로 6, 1층 (신정동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5202702, 126.860096),
    Restaurant("럭셔리한우축산", "서울특별시 구로구 개봉로3길 50 (개봉동)", None, "식육판매업", "우리동네 모범정육점", 37.4863305, 126.853501),
    Restaurant("축산사랑", "서울특별시 은평구 불광로109", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.6165063, 126.932540),
    Restaurant("영천(푸와주)", "서울특별시 성북구 아리랑로19길 34 (정릉동)", "02-915-3509", "식육판매업", "우리동네 모범정육점", 37.6025697, 127.011563),
    Restaurant("농장정육점", "서울특별시 금천구 독산로74길 18 (독산동 1021-2)", None, "식육판매업", "우리동네 모범정육점", 37.4705985, 126.909424),
    Restaurant("우림축산", "서울특별시 양천구 목동동로 377 (목동)", "02-2658-5705", "식육판매업", "우리동네 모범정육점", 37.5332644, 126.872398),
    Restaurant("우리바다양식", "서울특별시 강북구 덕릉로30길 14 (미아동)", "02-982-1315", "수산물판매업", "우리동네 수산물가공엋", 37.6267719, 127.027997),
    Restaurant("선일", "서울특별시 영등포구 도림로64가길 2 (대림동)", "02-832-8900", "식육판매업", "우리동네 모범정육점", 37.4964300, 126.905171),
    Restaurant("충남정육점", "서울특별시 중구 퇴계로85길 27, 1층(황학동)", None, "식육판매업", "우리동네 모범정육점", 37.5669887, 127.019493),
    Restaurant("청구일등축산", "서울특별시 중구 다산로 184, 1층(신당동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5597005, 127.013685),
    Restaurant("푸른목장", "서울특별시 동작구 상도로 102, 성대시장 1층 (상도동)", "02-822-6310", "식육판매업", "우리동네 모범정육점", 37.4998546, 126.932025),
    Restaurant("금천외양간", "서울특별시 금천구 독산로204", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4654693, 126.902487),
    Restaurant("박서방네", "서울특별시 강동구 풍성로 54길 27, 1층 (성내동)", "02-485-4945", "식육즉석판매가공업", "우리동네 모범정육점", 37.5282455, 127.133566),
    Restaurant("㈜아울렛마트", "서울특별시 금천구 독산로40길 29", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4605889, 126.906189),
    Restaurant("싱싱정육점", "서울특별시 강서구 양천로28길 29, 상가동 1층(방화동, 방화2차우림루미아트아파트)", "02-2663-8028", "식육즉석판매가공업", "우리동네 모범정육점", 37.5717992, 126.821308),
    Restaurant("고기샵정육점", "서울특별시 양천구 은행정로 6, 1층 (신정동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5202702, 126.860096),
    Restaurant("럭셔리한우축산", "서울특별시 구로구 개봉로3길 50 (개봉동)", None, "식육판매업", "우리동네 모범정육점", 37.4863305, 126.853501),
    Restaurant("축산사랑", "서울특별시 은평구 불광로109", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.6165063, 126.932540),
    Restaurant("영천(푸와주)", "서울특별시 성북구 아리랑로19길 34 (정릉동)", "02-915-3509", "식육판매업", "우리동네 모범정육점", 37.6025697, 127.011563),
    Restaurant("농장정육점", "서울특별시 금천구 독산로74길 18 (독산동 1021-2)", None, "식육판매업", "우리동네 모범정육점", 37.4705985, 126.909424),
    Restaurant("우림축산", "서울특별시 양천구 목동동로 377 (목동)", "02-2658-5705", "식육판매업", "우리동네 모범정육점", 37.5332644, 126.872398),
    Restaurant("우리바다양식", "서울특별시 강북구 덕릉로30길 14 (미아동)", "02-982-1315", "수산물판매업", "우리동네 수산물가공엋", 37.6267719, 127.027997),
    Restaurant("선일", "서울특별시 영등포구 도림로64가길 2 (대림동)", "02-832-8900", "식육판매업", "우리동네 모범정육점", 37.4964300, 126.905171),
    Restaurant("충남정육점", "서울특별시 중구 퇴계로85길 27, 1층(황학동)", None, "식육판매업", "우리동네 모범정육점", 37.5669887, 127.019493),
    Restaurant("청구일등축산", "서울특별시 중구 다산로 184, 1층(신당동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5597005, 127.013685),
    Restaurant("푸른목장", "서울특별시 동작구 상도로 102, 성대시장 1층 (상도동)", "02-822-6310", "식육판매업", "우리동네 모범정육점", 37.4998546, 126.932025),
    Restaurant("금천외양간", "서울특별시 금천구 독산로204", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4654693, 126.902487),
    Restaurant("박서방네", "서울특별시 강동구 풍성로 54길 27, 1층 (성내동)", "02-485-4945", "식육즉석판매가공업", "우리동네 모범정육점", 37.5282455, 127.133566),
    Restaurant("㈜아울렛마트", "서울특별시 금천구 독산로40길 29", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4605889, 126.906189),
    Restaurant("싱싱정육점", "서울특별시 강서구 양천로28길 29, 상가동 1층(방화동, 방화2차우림루미아트아파트)", "02-2663-8028", "식육즉석판매가공업", "우리동네 모범정육점", 37.5717992, 126.821308),
    Restaurant("고기샵정육점", "서울특별시 양천구 은행정로 6, 1층 (신정동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5202702, 126.860096),
    Restaurant("럭셔리한우축산", "서울특별시 구로구 개봉로3길 50 (개봉동)", None, "식육판매업", "우리동네 모범정육점", 37.4863305, 126.853501),
    Restaurant("축산사랑", "서울특별시 은평구 불광로109", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.6165063, 126.932540),
    Restaurant("영천(푸와주)", "서울특별시 성북구 아리랑로19길 34 (정릉동)", "02-915-3509", "식육판매업", "우리동네 모범정육점", 37.6025697, 127.011563),
    Restaurant("농장정육점", "서울특별시 금천구 독산로74길 18 (독산동 1021-2)", None, "식육판매업", "우리동네 모범정육점", 37.4705985, 126.909424),
    Restaurant("우림축산", "서울특별시 양천구 목동동로 377 (목동)", "02-2658-5705", "식육판매업", "우리동네 모범정육점", 37.5332644, 126.872398),
    Restaurant("우리바다양식", "서울특별시 강북구 덕릉로30길 14 (미아동)", "02-982-1315", "수산물판매업", "우리동네 수산물가공엋", 37.6267719, 127.027997),
    Restaurant("선일", "서울특별시 영등포구 도림로64가길 2 (대림동)", "02-832-8900", "식육판매업", "우리동네 모범정육점", 37.4964300, 126.905171),
    Restaurant("충남정육점", "서울특별시 중구 퇴계로85길 27, 1층(황학동)", None, "식육판매업", "우리동네 모범정육점", 37.5669887, 127.019493),
    Restaurant("청구일등축산", "서울특별시 중구 다산로 184, 1층(신당동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5597005, 127.013685),
    Restaurant("푸른목장", "서울특별시 동작구 상도로 102, 성대시장 1층 (상도동)", "02-822-6310", "식육판매업", "우리동네 모범정육점", 37.4998546, 126.932025),
    Restaurant("금천외양간", "서울특별시 금천구 독산로204", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4654693, 126.902487),
    Restaurant("박서방네", "서울특별시 강동구 풍성로 54길 27, 1층 (성내동)", "02-485-4945", "식육즉석판매가공업", "우리동네 모범정육점", 37.5282455, 127.133566),
    Restaurant("㈜아울렛마트", "서울특별시 금천구 독산로40길 29", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4605889, 126.906189),
    Restaurant("싱싱정육점", "서울특별시 강서구 양천로28길 29, 상가동 1층(방화동, 방화2차우림루미아트아파트)", "02-2663-8028", "식육즉석판매가공업", "우리동네 모범정육점", 37.5717992, 126.821308),
    Restaurant("고기샵정육점", "서울특별시 양천구 은행정로 6, 1층 (신정동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5202702, 126.860096),
    Restaurant("럭셔리한우축산", "서울특별시 구로구 개봉로3길 50 (개봉동)", None, "식육판매업", "우리동네 모범정육점", 37.4863305, 126.853501),
    Restaurant("축산사랑", "서울특별시 은평구 불광로109", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.6165063, 126.932540),
    Restaurant("영천(푸와주)", "서울특별시 성북구 아리랑로19길 34 (정릉동)", "02-915-3509", "식육판매업", "우리동네 모범정육점", 37.6025697, 127.011563),
    Restaurant("농장정육점", "서울특별시 금천구 독산로74길 18 (독산동 1021-2)", None, "식육판매업", "우리동네 모범정육점", 37.4705985, 126.909424),
    Restaurant("우림축산", "서울특별시 양천구 목동동로 377 (목동)", "02-2658-5705", "식육판매업", "우리동네 모범정육점", 37.5332644, 126.872398),
    Restaurant("우리바다양식", "서울특별시 강북구 덕릉로30길 14 (미아동)", "02-982-1315", "수산물판매업", "우리동네 수산물가공엋", 37.6267719, 127.027997),
    Restaurant("㈜아울렛마트", "서울특별시 금천구 독산로40길 29", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4605889, 126.906189),
    Restaurant("싱싱정육점", "서울특별시 강서구 양천로28길 29, 상가동 1층(방화동, 방화2차우림루미아트아파트)", "02-2663-8028", "식육즉석판매가공업", "우리동네 모범정육점", 37.5717992, 126.821308),
    Restaurant("고기샵정육점", "서울특별시 양천구 은행정로 6, 1층 (신정동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5202702, 126.860096),
    Restaurant("럭셔리한우축산", "서울특별시 구로구 개봉로3길 50 (개봉동)", None, "식육판매업", "우리동네 모범정육점", 37.4863305, 126.853501),
    Restaurant("축산사랑", "서울특별시 은평구 불광로109", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.6165063, 126.932540),
    Restaurant("영천(푸와주)", "서울특별시 성북구 아리랑로19길 34 (정릉동)", "02-915-3509", "식육판매업", "우리동네 모범정육점", 37.6025697, 127.011563),
    Restaurant("농장정육점", "서울특별시 금천구 독산로74길 18 (독산동 1021-2)", None, "식육판매업", "우리동네 모범정육점", 37.4705985, 126.909424),
    Restaurant("우림축산", "서울특별시 양천구 목동동로 377 (목동)", "02-2658-5705", "식육판매업", "우리동네 모범정육점", 37.5332644, 126.872398),
    Restaurant("우리바다양식", "서울특별시 강북구 덕릉로30길 14 (미아동)", "02-982-1315", "수산물판매업", "우리동네 수산물가공엋", 37.6267719, 127.027997),
    Restaurant("선일", "서울특별시 영등포구 도림로64가길 2 (대림동)", "02-832-8900", "식육판매업", "우리동네 모범정육점", 37.4964300, 126.905171),
    Restaurant("충남정육점", "서울특별시 중구 퇴계로85길 27, 1층(황학동)", None, "식육판매업", "우리동네 모범정육점", 37.5669887, 127.019493),
    Restaurant("청구일등축산", "서울특별시 중구 다산로 184, 1층(신당동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5597005, 127.013685),
    Restaurant("푸른목장", "서울특별시 동작구 상도로 102, 성대시장 1층 (상도동)", "02-822-6310", "식육판매업", "우리동네 모범정육점", 37.4998546, 126.932025),
    Restaurant("금천외양간", "서울특별시 금천구 독산로204", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4654693, 126.902487),
    Restaurant("박서방네", "서울특별시 강동구 풍성로 54길 27, 1층 (성내동)", "02-485-4945", "식육즉석판매가공업", "우리동네 모범정육점", 37.5282455, 127.133566),
    Restaurant("㈜아울렛마트", "서울특별시 금천구 독산로40길 29", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4605889, 126.906189),
    Restaurant("싱싱정육점", "서울특별시 강서구 양천로28길 29, 상가동 1층(방화동, 방화2차우림루미아트아파트)", "02-2663-8028", "식육즉석판매가공업", "우리동네 모범정육점", 37.5717992, 126.821308),
    Restaurant("고기샵정육점", "서울특별시 양천구 은행정로 6, 1층 (신정동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5202702, 126.860096),
    Restaurant("럭셔리한우축산", "서울특별시 구로구 개봉로3길 50 (개봉동)", None, "식육판매업", "우리동네 모범정육점", 37.4863305, 126.853501),
    Restaurant("축산사랑", "서울특별시 은평구 불광로109", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.6165063, 126.932540),
    Restaurant("영천(푸와주)", "서울특별시 성북구 아리랑로19길 34 (정릉동)", "02-915-3509", "식육판매업", "우리동네 모범정육점", 37.6025697, 127.011563),
    Restaurant("농장정육점", "서울특별시 금천구 독산로74길 18 (독산동 1021-2)", None, "식육판매업", "우리동네 모범정육점", 37.4705985, 126.909424),
    Restaurant("우림축산", "서울특별시 양천구 목동동로 377 (목동)", "02-2658-5705", "식육판매업", "우리동네 모범정육점", 37.5332644, 126.872398),
    Restaurant("우리바다양식", "서울특별시 강북구 덕릉로30길 14 (미아동)", "02-982-1315", "수산물판매업", "우리동네 수산물가공엋", 37.6267719, 127.027997),
    Restaurant("축산사랑", "서울특별시 은평구 불광로109", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.6165063, 126.932540),
    Restaurant("영천(푸와주)", "서울특별시 성북구 아리랑로19길 34 (정릉동)", "02-915-3509", "식육판매업", "우리동네 모범정육점", 37.6025697, 127.011563),
    Restaurant("농장정육점", "서울특별시 금천구 독산로74길 18 (독산동 1021-2)", None, "식육판매업", "우리동네 모범정육점", 37.4705985, 126.909424),
    Restaurant("우림축산", "서울특별시 양천구 목동동로 377 (목동)", "02-2658-5705", "식육판매업", "우리동네 모범정육점", 37.5332644, 126.872398),
    Restaurant("우리바다양식", "서울특별시 강북구 덕릉로30길 14 (미아동)", "02-982-1315", "수산물판매업", "우리동네 수산물가공엋", 37.6267719, 127.027997),
    Restaurant("선일", "서울특별시 영등포구 도림로64가길 2 (대림동)", "02-832-8900", "식육판매업", "우리동네 모범정육점", 37.4964300, 126.905171),
    Restaurant("충남정육점", "서울특별시 중구 퇴계로85길 27, 1층(황학동)", None, "식육판매업", "우리동네 모범정육점", 37.5669887, 127.019493),
    Restaurant("청구일등축산", "서울특별시 중구 다산로 184, 1층(신당동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5597005, 127.013685),
    Restaurant("푸른목장", "서울특별시 동작구 상도로 102, 성대시장 1층 (상도동)", "02-822-6310", "식육판매업", "우리동네 모범정육점", 37.4998546, 126.932025),
    Restaurant("금천외양간", "서울특별시 금천구 독산로204", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4654693, 126.902487),
    Restaurant("박서방네", "서울특별시 강동구 풍성로 54길 27, 1층 (성내동)", "02-485-4945", "식육즉석판매가공업", "우리동네 모범정육점", 37.5282455, 127.133566),
    Restaurant("㈜아울렛마트", "서울특별시 금천구 독산로40길 29", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4605889, 126.906189),
    Restaurant("싱싱정육점", "서울특별시 강서구 양천로28길 29, 상가동 1층(방화동, 방화2차우림루미아트아파트)", "02-2663-8028", "식육즉석판매가공업", "우리동네 모범정육점", 37.5717992, 126.821308),
    Restaurant("고기샵정육점", "서울특별시 양천구 은행정로 6, 1층 (신정동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5202702, 126.860096),
    Restaurant("럭셔리한우축산", "서울특별시 구로구 개봉로3길 50 (개봉동)", None, "식육판매업", "우리동네 모범정육점", 37.4863305, 126.853501),
    Restaurant("축산사랑", "서울특별시 은평구 불광로109", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.6165063, 126.932540),
    Restaurant("영천(푸와주)", "서울특별시 성북구 아리랑로19길 34 (정릉동)", "02-915-3509", "식육판매업", "우리동네 모범정육점", 37.6025697, 127.011563),
    Restaurant("농장정육점", "서울특별시 금천구 독산로74길 18 (독산동 1021-2)", None, "식육판매업", "우리동네 모범정육점", 37.4705985, 126.909424),
    Restaurant("우림축산", "서울특별시 양천구 목동동로 377 (목동)", "02-2658-5705", "식육판매업", "우리동네 모범정육점", 37.5332644, 126.872398),
    Restaurant("우리바다양식", "서울특별시 강북구 덕릉로30길 14 (미아동)", "02-982-1315", "수산물판매업", "우리동네 수산물가공엋", 37.6267719, 127.027997),
    Restaurant("축산사랑", "서울특별시 은평구 불광로109", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.6165063, 126.932540),
    Restaurant("영천(푸와주)", "서울특별시 성북구 아리랑로19길 34 (정릉동)", "02-915-3509", "식육판매업", "우리동네 모범정육점", 37.6025697, 127.011563),
    Restaurant("농장정육점", "서울특별시 금천구 독산로74길 18 (독산동 1021-2)", None, "식육판매업", "우리동네 모범정육점", 37.4705985, 126.909424),
    Restaurant("우림축산", "서울특별시 양천구 목동동로 377 (목동)", "02-2658-5705", "식육판매업", "우리동네 모범정육점", 37.5332644, 126.872398),
    Restaurant("우리바다양식", "서울특별시 강북구 덕릉로30길 14 (미아동)", "02-982-1315", "수산물판매업", "우리동네 수산물가공엋", 37.6267719, 127.027997),
    Restaurant("선일", "서울특별시 영등포구 도림로64가길 2 (대림동)", "02-832-8900", "식육판매업", "우리동네 모범정육점", 37.4964300, 126.905171),
    Restaurant("충남정육점", "서울특별시 중구 퇴계로85길 27, 1층(황학동)", None, "식육판매업", "우리동네 모범정육점", 37.5669887, 127.019493),
    Restaurant("청구일등축산", "서울특별시 중구 다산로 184, 1층(신당동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5597005, 127.013685),
    Restaurant("푸른목장", "서울특별시 동작구 상도로 102, 성대시장 1층 (상도동)", "02-822-6310", "식육판매업", "우리동네 모범정육점", 37.4998546, 126.932025),
    Restaurant("금천외양간", "서울특별시 금천구 독산로204", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4654693, 126.902487),
    Restaurant("박서방네", "서울특별시 강동구 풍성로 54길 27, 1층 (성내동)", "02-485-4945", "식육즉석판매가공업", "우리동네 모범정육점", 37.5282455, 127.133566),
    Restaurant("㈜아울렛마트", "서울특별시 금천구 독산로40길 29", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4605889, 126.906189),
    Restaurant("싱싱정육점", "서울특별시 강서구 양천로28길 29, 상가동 1층(방화동, 방화2차우림루미아트아파트)", "02-2663-8028", "식육즉석판매가공업", "우리동네 모범정육점", 37.5717992, 126.821308),
    Restaurant("고기샵정육점", "서울특별시 양천구 은행정로 6, 1층 (신정동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5202702, 126.860096),
    Restaurant("럭셔리한우축산", "서울특별시 구로구 개봉로3길 50 (개봉동)", None, "식육판매업", "우리동네 모범정육점", 37.4863305, 126.853501),
    Restaurant("축산사랑", "서울특별시 은평구 불광로109", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.6165063, 126.932540),
    Restaurant("영천(푸와주)", "서울특별시 성북구 아리랑로19길 34 (정릉동)", "02-915-3509", "식육판매업", "우리동네 모범정육점", 37.6025697, 127.011563),
    Restaurant("농장정육점", "서울특별시 금천구 독산로74길 18 (독산동 1021-2)", None, "식육판매업", "우리동네 모범정육점", 37.4705985, 126.909424),
    Restaurant("우림축산", "서울특별시 양천구 목동동로 377 (목동)", "02-2658-5705", "식육판매업", "우리동네 모범정육점", 37.5332644, 126.872398),
    Restaurant("우리바다양식", "서울특별시 강북구 덕릉로30길 14 (미아동)", "02-982-1315", "수산물판매업", "우리동네 수산물가공엋", 37.6267719, 127.027997),
    Restaurant("축산사랑", "서울특별시 은평구 불광로109", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.6165063, 126.932540),
    Restaurant("영천(푸와주)", "서울특별시 성북구 아리랑로19길 34 (정릉동)", "02-915-3509", "식육판매업", "우리동네 모범정육점", 37.6025697, 127.011563),
    Restaurant("농장정육점", "서울특별시 금천구 독산로74길 18 (독산동 1021-2)", None, "식육판매업", "우리동네 모범정육점", 37.4705985, 126.909424),
    Restaurant("우림축산", "서울특별시 양천구 목동동로 377 (목동)", "02-2658-5705", "식육판매업", "우리동네 모범정육점", 37.5332644, 126.872398),
    Restaurant("우리바다양식", "서울특별시 강북구 덕릉로30길 14 (미아동)", "02-982-1315", "수산물판매업", "우리동네 수산물가공엋", 37.6267719, 127.027997),
    Restaurant("선일", "서울특별시 영등포구 도림로64가길 2 (대림동)", "02-832-8900", "식육판매업", "우리동네 모범정육점", 37.4964300, 126.905171),
    Restaurant("충남정육점", "서울특별시 중구 퇴계로85길 27, 1층(황학동)", None, "식육판매업", "우리동네 모범정육점", 37.5669887, 127.019493),
    Restaurant("청구일등축산", "서울특별시 중구 다산로 184, 1층(신당동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5597005, 127.013685),
    Restaurant("푸른목장", "서울특별시 동작구 상도로 102, 성대시장 1층 (상도동)", "02-822-6310", "식육판매업", "우리동네 모범정육점", 37.4998546, 126.932025),
    Restaurant("금천외양간", "서울특별시 금천구 독산로204", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4654693, 126.902487),
    Restaurant("박서방네", "서울특별시 강동구 풍성로 54길 27, 1층 (성내동)", "02-485-4945", "식육즉석판매가공업", "우리동네 모범정육점", 37.5282455, 127.133566),
    Restaurant("㈜아울렛마트", "서울특별시 금천구 독산로40길 29", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.4605889, 126.906189),
    Restaurant("싱싱정육점", "서울특별시 강서구 양천로28길 29, 상가동 1층(방화동, 방화2차우림루미아트아파트)", "02-2663-8028", "식육즉석판매가공업", "우리동네 모범정육점", 37.5717992, 126.821308),
    Restaurant("고기샵정육점", "서울특별시 양천구 은행정로 6, 1층 (신정동)", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.5202702, 126.860096),
    Restaurant("럭셔리한우축산", "서울특별시 구로구 개봉로3길 50 (개봉동)", None, "식육판매업", "우리동네 모범정육점", 37.4863305, 126.853501),
    Restaurant("축산사랑", "서울특별시 은평구 불광로109", None, "식육즉석판매가공업", "우리동네 모범정육점", 37.6165063, 126.932540),
    Restaurant("영천(푸와주)", "서울특별시 성북구 아리랑로19길 34 (정릉동)", "02-915-3509", "식육판매업", "우리동네 모범정육점", 37.6025697, 127.011563),
    Restaurant("농장정육점", "서울특별시 금천구 독산로74길 18 (독산동 1021-2)", None, "식육판매업", "우리동네 모범정육점", 37.4705985, 126.909424),
    Restaurant("우림축산", "서울특별시 양천구 목동동로 377 (목동)", "02-2658-5705", "식육판매업", "우리동네 모범정육점", 37.5332644, 126.872398),
    Restaurant("우리바다양식", "서울특별시 강북구 덕릉로30길 14 (미아동)", "02-982-1315", "수산물판매업", "우리동네 수산물가공엋", 37.6267719, 127.027997),
]

# Route for home page
@app.route('/')
def index():
    return render_template('index.html', restaurants=restaurants)

# Dynamic route for displaying restaurant details
@app.route('/restaurant/<int:restaurant_id>')
def restaurant_detail(restaurant_id):
    restaurant = restaurants[restaurant_id]
    return render_template('restaurant_detail.html', restaurant=restaurant)

# API endpoint to get restaurant data
@app.route('/api/restaurants')
def get_restaurants():
    return jsonify([vars(restaurant) for restaurant in restaurants])

# Search functionality
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query').lower()
        results = [restaurant for restaurant in restaurants if query in restaurant.name.lower()]
        return render_template('search_results.html', query=query, results=results)
    return render_template('search.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)