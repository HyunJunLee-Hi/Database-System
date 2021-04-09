#-*- coding:utf-8 -*-
'''
관리자 99999999로 고유번호
ID는 -1이 되면 안된다
'''
#등록일 자동 설정
from datetime import datetime


            
#Interface
print("-------PlayList-------\n\n")

while 1:
    print("-------< Menu >-------")
    print("1. 로그인\n2. 회원가입\n3. 끝내기\n\n\n0. 관리자모드\n\n")

    MenuSelect = input("Select : ")
    print("\n")

    #Login page
    if MenuSelect=='1':
        while 1:
            print("<Log In>\n")
            print("뒤로가려면 -1을 입력하세요\n")      
            userID = input("ID : ")
            if userID == '-1':      
                break
            userPW = input("PW : ")

            #check ID and PW

            if userID !="" and userPW != "":        
                import pymysql as pms
                host = 'localhost'
                port = 3306
                user = 'db'
                psw = 'db!'
                charset = 'utf8'
                db = 'playlist'
                connection = pms.connect(host, user, psw, db, port, charset=charset)
                print("로딩...")


                
                try :
                    with connection.cursor() as cursor:
                        sql = "select * from 사용자 where (사용자_ID = %s and 사용자_비밀번호 = %s)"
                        cursor.execute(sql, (userID, userPW))
                        
                        result=cursor.fetchall()
                        
                        if(result):
                            #Use user name
                            print("\n-------<%s님 환영합니다>-------\n" %result[0][3])
                            while 1:
                                #Menu page
                                print("\n1. 음악 검색\n2. 앨범 검색\n3. 가수 검색\n4. 플레이리스트\n5. 끝내기\n\n\n0. 회원탈퇴\n")
                                userSelect = input("Select : ")
                                #Search music
                                if userSelect == '1':                                    
                                    while 1:
                                        print("\n1. 전체 음악 목록\n2. 제목으로 음악 검색\n0. 뒤로가기")
                                        musicSelect = input("Select : ")
                                        #Show every music
                                        if musicSelect == '1':
                                            #join for search singer name
                                            sql = "select 음악제목, 가수이름, 음악길이, 작곡가, 타이틀곡 from 가수, 앨범, 음악 where 가수_고유번호=가수번호 AND 앨범_고유번호 = 앨범번호"
                                            sql2 = "select count(*) from 음악"
                                            cursor.execute(sql)
                                            musiclist = cursor.fetchall()
                                            cursor.execute(sql2)
                                            musicCount = cursor.fetchall()      #For total number
                                            print("\n검색된 음악은 총 %s개 입니다\n" %musicCount[0][0])
                                            for row in musiclist:
                                                print("\n음악제목 : %s\t\t\t가수이름 : %s\t\t\t음악길이 : %s\t\t\t작곡가 : %s\t\t\t타이틀곡 : %s"%(row[0],row[1],row[2],row[3], row[4]))
                                        #search music
                                        elif musicSelect == '2':
                                            musicSearch = input("검색하고 싶은 음악을 입력해주세요 : ")
                                            if musicSearch != "":
                                                sql = "select 음악제목, 가수이름, 음악길이, 작곡가, 타이틀곡 from 가수, 앨범, 음악 where 가수_고유번호=가수번호 AND 앨범_고유번호 = 앨범번호 AND 음악제목 = %s"
                                                cursor.execute(sql, musicSearch)
                                                Smusic = cursor.fetchall()
                                                if(Smusic):
                                                    for row in Smusic:
                                                        print("\n음악제목 : %s\t\t\t가수이름 : %s\t\t\t음악길이 : %s\t\t\t작곡가 : %s\t\t\t타이틀곡 : %s"%(row[0],row[1],row[2],row[3], row[4]))
                                                else:
                                                    print("\n<음악을 찾을 수 없습니다>\n")
                                            else:
                                                print("\n<음악을 찾을 수 없습니다>\n")

                                        elif musicSelect == '0':
                                            break
                                        
                                        else:
                                            print("<Error : No menu>\n")
                                #Search album     
                                elif userSelect == '2':
                                    while 1:
                                        print("\n1. 전체 앨범 목록\n2. 제목으로 앨범 검색\n0. 뒤로가기")
                                        albumSelect = input("Select : ")
                                        if albumSelect == '1':
                                            sql = "select 앨범제목, 가수이름, count(*) from 앨범, 가수, 음악 where 가수_고유번호 = 가수번호 and 앨범_고유번호 = 앨범번호 group by 앨범_고유번호"
                                            sql2 = "select count(*) from 앨범"
                                            cursor.execute(sql)
                                            albumlist = cursor.fetchall()
                                            cursor.execute(sql2)
                                            albumCount = cursor.fetchall()
                                            print("\n검색된 앨범은 총 %s개 입니다\n" %albumCount[0][0])
                                            N1=int(1)
                                            for row in albumlist:
                                                print("\n%d번\t\t\t앨범제목 : %s\t\t\t가수이름 : %s\t\t\t총 : %s곡"%(N1,row[0],row[1],row[2]))
                                                N1 += 1
                                        elif albumSelect == '2':
                                            albumSearch = input("검색하고 싶은 앨범을 입력해주세요 : ")
                                            if  albumSearch != "":
                                                sql3 = "select 앨범제목, 가수이름, count(*) from 앨범, 가수, 음악 where 가수_고유번호 = 가수번호 and 앨범_고유번호 = 앨범번호 AND 앨범제목 = %s group by 앨범_고유번호"
                                                cursor.execute(sql3, albumSearch)
                                                Salbum = cursor.fetchall()
                                              
                                                if(Salbum):
                                                    N2=1
                                                    for row in Salbum:
                                                        print("\n%d번\t\t\t앨범제목 : %s\t\t\t가수이름 : %s\t\t\t총 : %s곡"%(N2,row[0],row[1],row[2]))
                                                        N2 += 1
                                                else:
                                                    print("\n<앨범을 찾을 수 없습니다>\n")
                                            else:
                                                print("\n<앨범을 찾을 수 없습니다>\n")
                                            
                                        elif albumSelect == '0':
                                            break
                                        else:
                                            print("<Error : No menu>\n")
                                #Search singer
                                elif userSelect == '3':
                                    while 1:
                                        print("\n1. 전체 가수 목록\n2. 이름으로 가수 검색\n0. 뒤로가기")
                                        singerSelect = input("Select : ")
                                        if singerSelect == '1':
                                            sql4 = "select * from 가수"
                                            sql5 = "select count(*) from 가수"
                                            cursor.execute(sql4)
                                            singerlist = cursor.fetchall()
                                            cursor.execute(sql5)
                                            singerCount = cursor.fetchall()
                                            print("\n검색된 가수는 총 %s명 입니다\n" %singerCount[0][0])
                                            for row in singerlist:
                                                print("\n%s\t\t\t%s\t\t\t%s\t\t\t%s"%(row[1],row[2],row[3],row[4]))
                                        elif singerSelect == '2':
                                            singerSearch = input("검색하고 싶은 가수를 입력해주세요 : ")
                                            if singerSearch != "":
                                                sql6 = "select * from 가수 where (가수이름 = %s)"
                                                cursor.execute(sql6, singerSearch)
                                                Ssinger = cursor.fetchall()
                                                if(Ssinger):
                                                    for row in Ssinger:
                                                        print("\n%s\t\t\t%s\t\t\t%s\t\t\t%s"%(row[1],row[2],row[3],row[4]))
                                                else:
                                                    print("\n<가수를 찾을 수 없습니다>\n")
                                            else:
                                                print("\n<가수를 찾을 수 없습니다>\n")
                                            
                                        elif singerSelect == '0':
                                            break
                                        else:
                                            print("<Error : No menu>\n")






                                #Playlist
                                elif userSelect == '4':
                                    while 1:
                                        sql1 = "select 고유등록번호, 리스트_고유번호 from 사용자, 플레이리스트 where 고유등록번호 = 사용자번호 AND 사용자_ID = %s"
                                        cursor.execute(sql1, userID)
                                        checkPL = cursor.fetchall()
                                        #check playlist exists
                                        if(checkPL):
                                            sql = "select 음악제목, 가수이름, 음악길이, 작곡가, 타이틀곡, 리스트_고유번호, 플레이리스트_음악.앨범번호, 플레이리스트_음악.트랙번호 from 사용자, 플레이리스트, 플레이리스트_음악, 음악, 앨범, 가수 where 가수_고유번호=앨범.가수번호 AND 앨범_고유번호 = 음악.앨범번호 AND 고유등록번호 = 사용자번호 AND 리스트_고유번호 = 리스트번호 AND 음악.앨범번호 = 플레이리스트_음악.앨범번호 AND 음악.트랙번호 = 플레이리스트_음악.트랙번호 AND 사용자_ID = %s"
                                            cursor.execute(sql, userID)
                                            PL=cursor.fetchall()
                                            PLNum = int(1)
                                            for row in PL:
                                                 print("Num : %d\t\t\t음악제목 : %s\t\t\t가수이름 : %s\t\t\t음악길이 : %s\t\t\t작곡가 : %s\t\t\t타이틀곡 : %s" %(PLNum, row[0], row[1], row[2], row[3], row[4]))
                                                 PLNum += 1
                                            plSelect = input("음악을 추가하려면 '1'/ 삭제하려면 '2' / 뒤로가려면 '0'을 입력해주세요 : ")
                                            if plSelect == '1':

                                                sqla = "select 음악제목, 가수이름, 음악길이, 작곡가, 타이틀곡 from 가수, 앨범, 음악 where 가수_고유번호=가수번호 AND 앨범_고유번호 = 앨범번호"
                                                cursor.execute(sqla)
                                                musiclist = cursor.fetchall()
                                                for row in musiclist:
                                                    print("\n음악제목 : %s\t\t\t가수이름 : %s\t\t\t음악길이 : %s\t\t\t작곡가 : %s\t\t\t타이틀곡 : %s"%(row[0],row[1],row[2],row[3], row[4]))
                                                    
                                                    

                                                musicName = input("\n\n추가할 음악의 이름을 입력해주세요 : ")
                                                    
                                                    
                                                if musicName != "":
                                                    sql3 = "select 음악제목, 가수이름, 음악길이, 작곡가, 타이틀곡, 앨범번호, 트랙번호 from 가수, 앨범, 음악 where 가수_고유번호=가수번호 AND 앨범_고유번호 = 앨범번호 AND 음악제목 = %s"
                                                    cursor.execute(sql3, musicName)
                                                    musicAdd = cursor.fetchall()
                                                    countAdd = int(0)
                                                    for i in musicAdd:
                                                        countAdd += 1
                                                 
                                                        
                                                    
                                                    MusicSelectNum = int(1)

                                                    #두개 이상일 때
                                                    if(countAdd > 1):
                                                        for row in musicAdd:
                                                            print("\nlist %s\t\t\t음악제목 : %s\t\t\t가수이름 : %s\t\t\t음악길이 : %s\t\t\t작곡가 : %s\t\t\t타이틀곡 : %s" %(MusicSelectNum, row[0], row[1], row[2], row[3], row[4]))
                                                            MusicSelectNum += 1
                                                        #int로 변형 가능한지(공백 등을 check)
                                                        try:
                                                            selectNum = int(input("추가를 원하는 list 번호를 입력해주세요 : "))
                                                        except ValueError:
                                                            print("숫자가 아닙니다")
                                                            break
                                                        #중복 체크
                                                        sqlc = "select 트랙번호 from 플레이리스트_음악 where 리스트번호 = %s and 앨범번호 = %s and 트랙번호 = %s"
                                                        cursor.execute(sqlc, (checkPL[0][1], musicAdd[(selectNum)-1][5], musicAdd[selectNum-1][6]))
                                                        checkdup = cursor.fetchall()
                                                        if(checkdup):
                                                            print("<Error : 중복된 노래입니다>")
                                                        else :
                                                            sql4 = "INSERT INTO 플레이리스트_음악 VALUES(%s, %s, %s)"
                                                            cursor.execute(sql4, (checkPL[0][1], musicAdd[selectNum-1][5], musicAdd[selectNum-1][6]))
                                                            connection.commit()
                                                            
                                                    #검색 결과가 하나일 때
                                                    elif(countAdd == 1):
                                                        #중복 check
                                                        sqlc = "select 트랙번호 from 플레이리스트_음악 where 리스트번호 = %s and 앨범번호 = %s and 트랙번호 = %s"
                                                        cursor.execute(sqlc, (checkPL[0][1], musicAdd[0][5], musicAdd[0][6]))
                                                        checkdup = cursor.fetchall()
                                                        if(checkdup):
                                                            print("<Error : 중복된 노래입니다>")
                                                        else :
                                                            
                                                        
                                                            sql4 = "INSERT INTO 플레이리스트_음악(리스트번호, 앨범번호, 트랙번호) VALUES(%s, %s, %s)"
                                                            cursor.execute(sql4, (checkPL[0][1], musicAdd[0][5], musicAdd[0][6]))
                                                            connection.commit()
                                                    
                                                    else :
                                                         print("\n음악을 찾을 수 없습니다.\n")
                                                    

                                                else :
                                                    print("\n<음악을 찾을 수 없습니다>\n")
                                            #delete music   
                                            elif plSelect == '2':
                                                try :
                                                    musicName = int(input("삭제할 음악의 번호를 입력해주세요 : "))
                                                except ValueError:
                                                    print("숫자가 아닙니다")
                                                    break
                                                if musicName != "":
                                                    
                                                    sql5 = "delete from 플레이리스트_음악 where 플레이리스트_음악.리스트번호 = %s AND 플레이리스트_음악.앨범번호 =%s AND 플레이리스트_음악.트랙번호 = %s"
                                                    cursor.execute(sql5, (PL[(musicName)-1][5],PL[(musicName)-1][6],PL[(musicName)-1][7]))
                                                    connection.commit()
                                                else:
                                                    print("<Error : 번호가 없습니다>")
                                                    
                                            
                                            elif plSelect == '0':
                                                break
                                            else :
                                                 print("<Error : No menu>")

                                         
                                        else :
                                            sql2 = "INSERT INTO 플레이리스트(사용자번호) VALUES(%s)"
                                            cursor.execute(sql2, result[0][0])
                                            #플레이리스트가 없다면 새로 생성 후 보여 줌
                                            connection.commit()
                                            print("\n<Playlist 생성완료>\n\n\n")
                                            
                                            
                                                
                                        
                                elif userSelect == '5':
                                    break

                                

                                #회원탈퇴
                                elif userSelect == '0':
                                    while 1:
                                        yn = input("정말로 탈퇴하시겠습니까? (y/n) : ")
                                        if (yn !="" and yn == y):
                                            sqlx = "delete from 사용자 where 고유등록번호 = %s"
                                            cursor.execute(sqlx, (result[0][0]))
                                            connection.commit()
                                            exit()
                                        elif (yn !="" and yn == n):
                                            break
                                        else :
                                            print("y 또는 n을 입력해주세요")
                                else :
                                    print("<Error : No menu>")
                        else:
                            print("\n<아이디나 비밀번호가 틀렸거나 등록이 안되있습니다>\n\n")
                          
                        connection.commit()
                finally:
                    connection.close()
                    
    #회원가입
    if MenuSelect=='2':
        while 1:
            print("-------회원가입-------")
            print("뒤로가려면 -1을 입력하세요\n")
            newuserID = input("원하는 ID를 입력하세요 : ")
            if newuserID == '-1':
                break
            import pymysql as pms
            host = 'localhost'
            port = 3306
            user = 'db'
            psw = 'db!'
            charset = 'utf8'
            db = 'playlist'
            connection = pms.connect(host, user, psw, db, port, charset=charset)
            
            #중복 체크
            with connection.cursor() as cursor:
                sql = "select 사용자_ID from 사용자 where (사용자_ID = %s)"
                cursor.execute(sql, (newuserID))
                result=cursor.fetchall()
                if(result):
                    print("\nError : 중복되는 ID입니다!\n\n")
                    
                else:
                    newuserPW=input("사용하실 PW를 입력해주세요 : ")
                    newuserPW2=input("사용하실 PW를 한번 더 입력해주세요 : ")
                    if newuserID!="" and newuserPW!="" and newuserPW2!="":                
                        if(newuserPW == newuserPW2):
                            userName=input("이름을 입력해주세요 : ")
                            userAge = input("나이를 입력해주세요(ex:24) : ")
                            userSex = input("성별을 입력해주세요(ex:F or M) : ")
                            userBdate = input("생일을 입력해주세요(ex:1996-04-30) : ")
                            userAdd = input("주소를 입력해주세요 : ")

                            sql = "INSERT INTO 사용자(사용자_ID, 사용자_비밀번호, 이름, 나이, 성별, 생일, 주소, 등록일, 관리자번호) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            cursor.execute(sql, (newuserID, newuserPW, userName, userAge, userSex, userBdate, userAdd, datetime.today().strftime("%Y-%m-%d"),'99999999'))
                            connection.commit()

                            print("회원가입 완료\n")
                            break
            
                        else:
                            print("PW가 일치하지 않습니다!\n")
                        
                          

            
    #프로그램 종료
    if MenuSelect=='3':
        break

    #관리자 모드
    if MenuSelect=='0':
        while 1:
            print("\n-------관리자모드-------\n\n")
            import pymysql as pms
            host = 'localhost'
            port = 3306
            user = 'db'
            psw = 'db!'
            charset = 'utf8'
            db = 'playlist'
            connection = pms.connect(host, user, psw, db, port, charset=charset)

            print("뒤로가려면 -1을 입력하세요\n")
            #뒤로가기
            rootID=input("ID : ")
            if rootID == '-1':
                break
            rootPW=input("PW : ")
            #로그인
            if rootID !="" and rootPW!="":
                with connection.cursor() as cursor:
                    sql = "select * from 관리자 where (관리자_ID = %s and 관리자_비밀번호 = %s)"
                    cursor.execute(sql, (rootID, rootPW))
                    result=cursor.fetchall()
                    if(result):
                        while 1:
                            print("\n1. User Management\n2. Album Management\n3. Music Management\n4. Singer Management\n5. Back")
                            mgSelect = input("Select : ")
                            #사용자 관리
                            if mgSelect == '1':
                                while 1:
                                    print("\n-------<User Management>-------\n\n")
                                    print("1. Show every user\n2. User delete\n3. Back")
                                    Muser = input("Select : ")
                                    #전체 사용자 확인
                                    if Muser == '1':
                                        sql1 = "select * from 사용자"
                                        cursor.execute(sql1)
                                        userlist = cursor.fetchall()
                                        userN = int(1)
                                        for row in userlist:
                                            print("(%d)\t%s/%s/%s/%s/%s/%s/%s/%s/%s" %(userN, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
                                            userN += 1
                                    #사용자 삭제
                                    elif Muser == '2':
                                        sql1 = "select * from 사용자"
                                        cursor.execute(sql1)
                                        userlist = cursor.fetchall()
                                        userN = int(1)
                                        for row in userlist:
                                            print("(%d)\t%s/%s/%s/%s/%s/%s/%s/%s/%s" %(userN, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
                                            userN += 1
                                        #번호로 사용자 지정 후 삭제
                                        try :
                                            deleteUser = int(input("\n삭제하고싶은 사용자의 번호를 입력해주세요 : "))
                                        except ValueError:
                                            print("숫자가 아닙니다")
                                            break
                                        if((deleteUser) > userN):
                                            print("Wrong user number")
                                        else :
                                            sql2 = "delete from 사용자 where 고유등록번호 = %s"
                                            cursor.execute(sql2, userlist[(deleteUser)-1][0])
                                            connection.commit()
                                                           
                                    elif Muser == '3':
                                        break
                                    else:
                                        print("<Error : No menu>")
                            #앨범 관리
                            elif mgSelect == '2':
                                while 1:
                                    print("\n-------<Album Management>-------\n")
                                    print("1. Show every album\n2. Album delete\n3. Back")
                                    Malbum = input("Select : ")
                                    #전체 앨범 확인
                                    if Malbum == '1':
                                        sql1 = "select 앨범_고유번호, 앨범제목, 가수이름 from 가수, 앨범 where 가수_고유번호 = 가수번호"
                                        cursor.execute(sql1)
                                        albumlist = cursor.fetchall()
                                        albumN = int(1)
                                        for row in albumlist:
                                            print("(%d)\t%s/%s/%s" %(albumN, row[0], row[1], row[2]))
                                            albumN += 1
                                    #앨범 삭제
                                    elif Malbum == '2':
                                        sql1 = "select 앨범_고유번호, 앨범제목, 가수이름 from 가수, 앨범 where 가수_고유번호 = 가수번호"
                                        cursor.execute(sql1)
                                        albumlist = cursor.fetchall()
                                        albumN = int(1)
                                        for row in albumlist:
                                            print("(%d)\t%s/%s/%s" %(albumN, row[0], row[1], row[2]))
                                            albumN += 1
                                        try :
                                            deletealbum = int(input("\n삭제하고싶은 앨범의 번호를 입력해주세요 : "))
                                        except ValueError:
                                            print("숫자가 아닙니다")
                                            break
                                        if((deletealbum) > albumN):
                                            print("Wrong album number")
                                        else :
                                            sql2 = "delete from 앨범 where 앨범_고유번호 = %s"
                                            cursor.execute(sql2, albumlist[(deletealbum)-1][0])
                                            connection.commit()
                                                           
                                    elif Malbum == '3':
                                        break
                                    else:
                                        print("<Error : No menu>")
                            #음악 관리    
                            elif mgSelect == '3':
                                while 1:
                                    print("\n-------<Music Management>-------\n\n")
                                    print("1. Show every music\n2. Music insert\n3. Music delete\n4. Back")
                                    Mmusic = input("Select : ")
                                    #전체 음악 확인
                                    if Mmusic == '1':
                                            sql1 = "select 음악제목, 가수이름, 음악길이, 작곡가, 타이틀곡 from 음악, 앨범, 가수 where 앨범_고유번호 = 음악.앨범번호 AND 가수_고유번호 = 앨범.가수번호"
                                            cursor.execute(sql1)
                                            musiclist = cursor.fetchall()
                                            musicN = int(1)
                                            for row in musiclist:
                                                print("(%d)\t%s/%s/%s/%s/%s" %(musicN, row[0], row[1], row[2], row[3], row[4]))
                                                musicN += 1

                                    elif Mmusic == '2':
                                        #가수가 있는지 확인 없으면 추가
                                        #앨범이 있는지 확인 없으면 추가
                                        #같은 음악인지 확인 (완전히 다 같아야함)
                                        #음악이 있으면 앨범이 있고 가수가 있어야함
                                        while 1:
                                            isregS =input("등록되어있는 가수입니까? (y/n) : ")
                                            #가수가 등록되어 있을 경우
                                            if isregS == 'y':
                                                whoissinger = input("가수 고유등록번호을 입력해주세요 : ")
                                                isregA = input("등록되어있는 앨범입니까? (y/n) : ")
                                                #앨범이 등록되어 있을 경우
                                                if isregA == 'y':
                                                    whatalbum = input("앨범 고유번호를 입력해주세요 : ")
                                                    sql1 = "select 가수이름, 앨범제목 from 가수, 앨범 where 가수_고유번호 = 가수번호 AND 가수_고유번호 = %s AND 앨범_고유번호 = %s"
                                                    cursor.execute(sql1, (whoissinger, whatalbum))
                                                    singeralbum = cursor.fetchall()
                                                    musicname = input("음악 제목을 입력해주세요 : ")
                                                    musictime = input("음악 길이를 입력해주세요 (ex: 3:30) : ")
                                                    musicprod = input("작곡가를 입력해주세요 : ")
                                                    istitle = input("타이틀 곡이면 Y / 아니면 N을 입력해주세요 : ")
                                                                    
                                                    sql2 = "INSERT INTO 음악(앨범번호, 음악제목, 음악길이, 작곡가, 타이틀곡) VALUES (%s, %s, %s, %s, %s)"
                                                    cursor.execute(sql2,(whatalbum, musicname, musictime, musicprod, istitle))
                                                    connection.commit()
                                                    break   
                                                #새로운 앨범인 경우                                                        
                                                elif isregA == 'n':
                                                    sql1 = "select 앨범_고유번호 from 앨범 order by 앨범_고유번호 DESC"
                                                    cursor.execute(sql1)
                                                    albumssn = cursor.fetchall()
                                                    #최초 앨범 고유번호 설정
                                                    if(albumssn) :
                                                        albumssn = int(albumssn[0][0]) + 1
                                                    else :
                                                        albumssn = int(70000001)
                                                    #앨범 등록
                                                    albumname = input("앨범 제목을 입력해주세요 : ")
                                                    sql3 = "INSERT INTO 앨범 VALUES (%s, %s, %s, %s)"
                                                    cursor.execute(sql3, (albumssn, albumname, 99999999, whoissinger))
                                                    
                                                    #음악 등록
                                                    musicname = input("음악 제목을 입력해주세요 : ")
                                                    musictime = input("음악 길이를 입력해주세요 (ex: 3:30) : ")
                                                    musicprod = input("작곡가를 입력해주세요 : ")
                                                    istitle = input("타이틀 곡이면 Y / 아니면 N을 입력해주세요 : ")
                                                                    
                                                    sql2 = "INSERT INTO 음악(앨범번호, 음악제목, 음악길이, 작곡가, 타이틀곡) VALUES (%s, %s, %s, %s, %s)"
                                                    cursor.execute(sql2,(albumssn, musicname, musictime, musicprod, istitle))
                                                    connection.commit()
                                                    print("\n<등록완료>\n")
                                                    break
                                                    
                                                else :
                                                    print("\n<다시 선택해주세요>\n")
                                            #가수가 등록되어있지 않을 경우(앨범과 노래 모두 등록 필요)
                                            elif isregS == 'n':
                                                sql1 = "select 가수_고유번호 from 가수 order by 가수_고유번호 DESC"
                                                cursor.execute(sql1)
                                                singerssn = cursor.fetchall()
                                                #최초 가수 고유번호 생성
                                                if(singerssn):
                                                    singerssn = int(singerssn[0][0]) + 1
                                                else :
                                                    singerssn = int(80000001)
                                                #가수 등록
                                                singername = input("가수이름을 입력해주세요 : ")
                                                singerbdate = input("가수 생일을 입력해주세요 (ex: 1998-09-09) : ")
                                                singerin = input("소속사를 입력해주세요 : ")
                                                singersex = input("성별을 입력해주세요 (F/M) : ")
                                                
                                                sql2 = "INSERT INTO 가수 VALUES (%s, %s, %s, %s, %s, %s)"
                                                cursor.execute(sql2, (singerssn, singername, singerbdate, singerin, singersex, 99999999))

                                                sql3 = "select 앨범_고유번호 from 앨범 order by 앨범_고유번호 DESC"
                                                cursor.execute(sql3)
                                                albumssn = cursor.fetchall()
                                                #최초 앨범 고유번호 생성
                                                if(albumssn) :
                                                    albumssn = int(albumssn[0][0]) + 1
                                                else :
                                                    albumssn = int(70000001)
                                                albumname = input("앨범 제목을 입력해주세요 : ")
                                                sql4 = "INSERT INTO 앨범 VALUES (%s, %s, %s, %s)"
                                                cursor.execute(sql4, (albumssn, albumname, 99999999, singerssn))
                                                    
                                                #음악 등록
                                                musicname = input("음악 제목을 입력해주세요 : ")
                                                musictime = input("음악 길이를 입력해주세요 (ex: 3:30) : ")
                                                musicprod = input("작곡가를 입력해주세요 : ")
                                                istitle = input("타이틀 곡이면 Y / 아니면 N을 입력해주세요 : ")
                                                                    
                                                sql5 = "INSERT INTO 음악(앨범번호, 음악제목, 음악길이, 작곡가, 타이틀곡) VALUES (%s, %s, %s, %s, %s)"
                                                cursor.execute(sql5,(albumssn, musicname, musictime, musicprod, istitle))
                                                connection.commit()
                                                print("\n<등록완료>\n")
                                                break

                                                
                                                               
                                            else :
                                                print("\n<다시 선택해주세요>\n")

                                            

                                            
                                        




                                    #음악 삭제
                                    elif Mmusic == '3':
                                        #전체 음악 목록
                                        sql1 = "select 음악제목, 가수이름, 음악길이, 작곡가, 타이틀곡, 앨범번호, 트랙번호 from 음악, 앨범, 가수 where 앨범_고유번호 = 음악.앨범번호 AND 가수_고유번호 = 앨범.가수번호"
                                        cursor.execute(sql1)
                                        musiclist = cursor.fetchall()
                                        musicN = int(1)
                                        for row in musiclist:
                                            print("(%d)\t%s/%s/%s/%s/%s" %(musicN, row[0], row[1], row[2], row[3], row[4]))
                                            musicN += 1

                                        try :
                                            deletemusic = int(input("\n삭제하고싶은 음악의 번호를 입력해주세요 : "))
                                        except ValueError:
                                            print("숫자가 아닙니다")
                                            break
                                        if((deletemusic) > musicN):
                                            print("Wrong music number")
                                        else :
                                          
                                            sql2 = "delete from 음악 where 앨범번호 = %s AND 트랙번호 = %s"
                                            cursor.execute(sql2, (musiclist[(deletemusic)-1][5], musiclist[(deletemusic)-1][6]))
                                            connection.commit()
                                    #종료  
                                    elif Mmusic == '4':
                                        break
                                    else:
                                        print("<Error : No menu>")
                            #가수 관리
                            elif mgSelect == '4':
                                while 1:
                                    print("\n-------<Singer Management>-------\n\n")
                                    print("1. Show every singer\n2. Singer delete\n3. Back")
                                    Msinger = input("Select : ")
                                    #전체 가수 목록
                                    if Msinger == '1':
                                        sql1 = "select * from 가수"
                                        cursor.execute(sql1)
                                        singerlist = cursor.fetchall()
                                        singerN = int(1)
                                        for row in singerlist:
                                            print("(%d)\t%s/%s/%s/%s/%s" %(singerN, row[0], row[1], row[2], row[3], row[4]))
                                            singerN += 1
                                    #가수 삭제
                                    elif Msinger == '2':
                                        sql1 = "select * from 가수"
                                        cursor.execute(sql1)
                                        singerlist = cursor.fetchall()
                                        singerN = int(1)
                                        for row in singerlist:
                                            print("(%d)\t%s/%s/%s/%s/%s" %(singerN, row[0], row[1], row[2], row[3], row[4]))
                                            singerN += 1

                                        try :
                                            deletesinger = int(input("\n삭제하고싶은 가수의 번호를 입력해주세요 : "))
                                        except ValueError:
                                            print("숫자가 아닙니다")
                                            break
                                        if((deletesinger) > singerN):
                                            print("Wrong singer number")
                                        else :
                                            sql2 = "delete from 가수 where 가수_고유번호 = %s"
                                            cursor.execute(sql2, singerlist[(deletesinger)-1][0])
                                            connection.commit()
                                                           
                                    elif Msinger == '3':
                                        break
                                    else:
                                        print("<Error : No menu>")
                                        
                            elif mgSelect == '5':
                                break
                            
                    else:
                        print("\nError : wrong ID or wrong PW")
            connection.commit()

            
      
