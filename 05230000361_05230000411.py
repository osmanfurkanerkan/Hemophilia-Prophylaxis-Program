def get_contestant_and_week_info():
    while True:
        try:
            # Kullanıcıdan yarışmacı sayısını aldık ve hata kontrolünü yaptık.
            contestant_count = int(input("Enter number of contestants (at least 5): "))
            while contestant_count < 5:
                print(" number of contestants must be at least 5.")
                contestant_count = int(input("Enter number of contestants (at least 5): "))

            # Kullanıcıdan yarışmanın hafta sayısını aldık ve hata kontrolünü yaptık.
            contest_duration_week = int(input("Enter duration of the contest (at least 3): "))
            while contest_duration_week < 3:
                print("duration of the contest must be at least 3 weeks.")
                contest_duration_week = int(input("Enter duration of the contest (at least 3): "))

            return contestant_count, contest_duration_week 
        # Geçerli bir sayı girilmediğinde hata mesajı gösterdik
        except ValueError:
            print("Please enter a valid number.")


def get_weekly_scores(contestant_count, number_of_coaches):
    # Koçlar tarafından verilen haftalık puanları ve izleyiciler tarafından verilen haftalık puanları saklamak için listeler oluşturduk
    weekly_scores_coach = []
    for i in range(number_of_coaches):
        weekly_scores_coach.append([0] * contestant_count) 
    weekly_scores_audience = [0] * contestant_count

    for coach in range(number_of_coaches):
        print(f"Coach {coach + 1} is giving points:")

        # Koçun puan verdiği yarışmacıları takip etmek için bir liste oluşturduk.
        given_contestants = []

        for points in range(1, 4):  # Her koç 1, 2, 3 puan verir, bu yüzden range(1, 4)
            while True:
                try:
                    # koçun puan vermesi için yarışmacı numarasını aldık.
                    contestant_number = int(input(f"Enter contestant number to give {points} points: "))
                    while contestant_number < 1 or contestant_number > contestant_count or contestant_number == coach + 1 or contestant_number in given_contestants:
                        print("Invalid contestant number. Please enter a valid number, and coaches cannot vote for themselves or the same contestant twice.")
                        contestant_number = int(input(f"Enter contestant number to give {points} points: "))

                    # Yarışmacıya puan ekledik ve bu yarışmacıyı puan verilenler listesine ekledik
                    weekly_scores_coach[coach][contestant_number - 1] += points
                    given_contestants.append(contestant_number)
                    break
                except ValueError:
                    # Geçersiz girişte hata mesajı gösterdik.
                    print("Invalid input. Please enter a valid number.")

    print("Audience is giving points:")
    for points in range(1, 4):  # İzleyiciler 1, 2, 3 puan verir, bu yüzden range(1, 4)
        while True:
            try:
                # Puan vermek için yarışmacı numarasını aldık.
                contestant_number = int(input(f"Enter contestant number to give {points} points: "))
                while contestant_number < 1 or contestant_number > contestant_count:
                    print("Invalid contestant number. Please enter a valid number.")
                    contestant_number = int(input(f"Enter contestant number to give {points} points: "))
                # Yarışmacıya seyircinin verdiği puanı ekledik.
                weekly_scores_audience[contestant_number - 1] += points
                break
            except ValueError:
                # Geçersiz girişte hata mesajı gösterdik.
                print("Invalid input. Please enter a valid contestant number.")

    return weekly_scores_coach, weekly_scores_audience

def calculate_weekly_total_scores(weekly_scores_coach, weekly_scores_audience, number_of_coaches):
    total_scores = []
    contestant_count = len(weekly_scores_audience)         #fonksiyonun içinde yarışmacı sayısını bir değişkene atamak için weekly_scores_audience listemizin uzunluğunu contestant_count'a atadık.
    for i in range(contestant_count):
        # Her bir yarışmacı için koçlardan gelen puanları hesapladık.
        coach_score = 0
        for coach in weekly_scores_coach:
            coach_score += coach[i]
        # Her bir yarışmacı için izleyicilerden gelen puanları hesapladık. Koçlardan ve izleyicilerden aldığı puanlar eşit ağırlıkla toplanması için izleyiciden gelen skoru yarışmacı sayısının 1 eksiği ile çarptık.
        audience_score = weekly_scores_audience[i] * (number_of_coaches - 1)  
        total_score = coach_score + audience_score
        # Yarışmacının numarası, koçtan gelen puanı, izleyiciden gelen puanı ve toplam puanı bir tuple olarak listeye ekledik.
        total_scores.append((i + 1, coach_score, audience_score, total_score))
    return total_scores

def display_weekly_results(total_scores, cumulative_scores=None):
    #haftalık sonuçları ilk olarak toplam puana, ardından koçtan gelen puana ve en son yarışmacı numarasına göre sıraladık.
    total_scores.sort(key=lambda x: (-x[3], -x[1], x[0]))  
    
    print(f"\nScoring results for week :")
    print("Rank | Contestant No | Coach Score | Audience Score  | Total Score")
    for rank, (contestant_no, coach_score, audience_score, total_score) in enumerate(total_scores, start=1):
        print(f"{rank:^4} | {contestant_no:^13} | {coach_score:^11} | {audience_score:^15} | {total_score:^11}")
    
    if cumulative_scores:
        print("\nOverall standings at the end of weeks :")
        #toplam puanı ilk olarak toplam puana, ardından koçtan gelen puana ve en son yarışmacı numarasına göre sıraladık.
        cumulative_scores.sort(key=lambda x: (-x[3], -x[1], x[0]))  
        print("Rank | Contestant No | Coach Score | Audience Score  | Total Score")
        for rank, (contestant_no, coach_score, audience_score, total_score) in enumerate(cumulative_scores, start=1):
            print(f"{rank:^4} | {contestant_no:^13} | {coach_score:^11} | {audience_score:^15} | {total_score:^11}")

def display_overall_standings(overall_coach_scores, overall_audience_scores, overall_total_scores):
    # Tüm puanları bir listeye ekledik ve her bir yarışmacının koçtan gelen puanını , izleyiciden gelen puanını ve total skoru total_scores listemizin içine tuple olarak ekledik
    total_scores = []
    for i in range(len(overall_total_scores)):
        total_scores.append((i + 1, overall_coach_scores[i], overall_audience_scores[i], overall_total_scores[i]))

    # Toplam puana, ardından koç puanına ve en son yarışmacı numarasına göre sıraladık.
    total_scores.sort(key=lambda x: (-x[3], -x[1], x[0]))

    print("\nOverall Standings:")
    print("Rank | Contestant No | Coach Score | Audience Score | Total Score")
    for rank, (contestant_no, coach_score, audience_score, total_score  ) in enumerate(total_scores, start=1):
        print(f"{rank:^4} | {contestant_no:^13} | {coach_score:^11} | {audience_score:^15} | {total_score:^11}")

    display_standings_by_coach_scores(overall_coach_scores)
    display_standings_by_audience_scores(overall_audience_scores)
    
def display_standings_by_coach_scores(overall_coach_scores):
    # Her bir yarışmacının koç puanlarını bir listeye ekledik
    coach_scores = [(i + 1, overall_coach_scores[i]) for i in range(len(overall_coach_scores))]
    # Koç puanlarına göre sıraladık.
    coach_scores.sort(key=lambda x: (-x[1], x[0]))

    print("\nOverall standings based on the coaches' scores only :")
    print("Rank | Contestant No | Score")
    for rank, (contestant_no, score) in enumerate(coach_scores, start=1):
        print(f"{rank:^4} | {contestant_no:^13} | {score:^5}")

def display_standings_by_audience_scores(overall_audience_scores):
    # Her bir yarışmacının izleyici puanlarını bir listeye ekledik.
    audience_scores = []
    for i in range(len(overall_audience_scores)):
        audience_scores.append((i + 1, overall_audience_scores[i]))

    # İzleyici puanlarına göre sıraladık.
    audience_scores.sort(key=lambda x: (-x[1], x[0]))

    print("\nOverall standings based on the audience scores only: ")
    print("Rank | Contestant No | Score")
    for rank, (contestant_no, score) in enumerate(audience_scores, start=1):
        print(f"{rank:^4} | {contestant_no:^13} | {score:^5}")

def display_weekly_championships(overall_total_scores, contest_duration_week, weekly_scores_history):
    # Her yarışmacı için haftalık şampiyonluklarını saklamak için bir liste oluşturduk.
    weekly_championships = [0] * len(overall_total_scores)

    for week_scores in weekly_scores_history:
        # Haftalık puanları sıralayarak her haftanın şampiyonunu belirledik.
        week_scores_sorted = sorted([(i + 1, score) for i, score in enumerate(week_scores)],key=lambda x: -x[1],)
        weekly_championships[week_scores_sorted[0][0] - 1] += 1  

    print("\nTotal scores for each week and the number of week championships of the contestants:")
    print("Contestant No | Week Championships|", end=" ")
    # Şampiyon olan yarışmacının şampiyonluk sayısını artırdık.
    for week in range(1, contest_duration_week + 1):
        print(f"Week {week}", end=" | ")
    print()

    for contestant_no, championships in enumerate(weekly_championships, start=1):
        # Yarışmacı numarası ve şampiyonluk sayılarını yazdırdık.
        print(f"{contestant_no:^13} | {championships:^17}", end=" |")
        for week in range(1, contest_duration_week + 1):
            print(f"{weekly_scores_history[week - 1][contestant_no - 1]:^7}", end=" |")
        print()

def display_scores_by_coach(overall_scores_by_coach, contestant_count, number_of_coaches):
    #bu fonksiyonda koçlardan gelen puanlara göre sıralamayı yaptık.
    print("\nTotal scores received by the contestants from the coaches:")
    print("Contestant No", end="")
    for coach in range(1, number_of_coaches + 1):
        # Her bir koç için başlık yazdırdık.
        print(f" | Coach-{coach} ", end="")
    print()

    for contestant_no in range(1, contestant_count + 1):
        # Yarışmacı numarasını yazdırdık.
        print(f"{contestant_no:^13}", end="")
        for coach in range(number_of_coaches):
            print(f" | {overall_scores_by_coach[coach][contestant_no - 1]:^8}", end="")
        print()


def start_competition():
    #bu fonksiyonda genel olarak yarışmanın diğer fonksiyonlarını çağırdık. main fonksiyonunda ise bu fonksiyonu çağırdık.
    # Yarışmacı sayısını ve yarışma süresini aldık aşağıda.
    contestant_count, contest_duration_week = get_contestant_and_week_info()
    number_of_coaches = contestant_count

    # Genel koç puanlarını, izleyici puanlarını ve toplam puanları saklamak için listeler oluşturduk.
    overall_coach_scores = [0] * contestant_count
    overall_audience_scores = [0] * contestant_count
    overall_total_scores = [0] * contestant_count
    weekly_scores_history = []  # Her haftanın toplam skorlarını tutmak için liste
    overall_scores_by_coach = []
    for i in range(number_of_coaches):
        overall_scores_by_coach.append([0] * contestant_count) # Koç puanları için yeni liste

    for week in range(1, contest_duration_week + 1):
        print(f"\nWeek {week}:")
        # Haftalık koç ve izleyici puanlarını aldık.
        weekly_scores_coach, weekly_scores_audience = get_weekly_scores(contestant_count, number_of_coaches)
        # Haftalık toplam puanları hesapla
        total_scores = calculate_weekly_total_scores(weekly_scores_coach, weekly_scores_audience, number_of_coaches)

        # Haftalık toplam skorları ve total skorları hesapladık.
        weekly_total = [0] * contestant_count
        for i, (a, coach_score, audience_score, total_score) in enumerate(total_scores):
            overall_coach_scores[i] += coach_score
            overall_audience_scores[i] += audience_score
            overall_total_scores[i] += total_score
            weekly_total[i] = total_score  # Haftalık toplamı weekly_total listemize kaydettik.

        # Koçların verdiği toplam puanları güncelledik.
        for coach in range(number_of_coaches):
            for contestant in range(contestant_count):
                overall_scores_by_coach[coach][contestant] += weekly_scores_coach[coach][contestant]

        weekly_scores_history.append(weekly_total)  # Haftalık skorları kaydet
        cumulative_scores = []
        for i in range(contestant_count):
            cumulative_scores.append((i + 1, overall_coach_scores[i], overall_audience_scores[i], overall_total_scores[i]))

        display_weekly_results(total_scores, cumulative_scores)

    print("\nCompetition Completed.")
    display_standings_by_coach_scores(overall_coach_scores)                                          # Koç puanlarına göre sıralamaları gösterdik
    display_standings_by_audience_scores(overall_audience_scores)                                    # İzleyici puanlarına göre sıralamaları göster
    display_weekly_championships(overall_total_scores, contest_duration_week, weekly_scores_history) # Haftalık şampiyonlukları gösterdik
    display_scores_by_coach(overall_scores_by_coach, contestant_count, number_of_coaches)            # Koçlardan alınan puanları gösterdik.
    return overall_coach_scores, overall_audience_scores, overall_total_scores

def main():
    while True:
        # Yarışmayı çalıştırdık ve genel puanları aldık.
        overall_coach_scores, overall_audience_scores, overall_total_scores = start_competition()

        # Kullanıcıya yeni bir yarışma isteyip istemediğini sorduk.
        while True:
            other_competition = input("Do you want to organize a new competition? (y/Y/n/N): ")

            if other_competition in ["N", "n"]:
                print("Exiting the program.")
                return 
            elif other_competition in ["y", "Y"]:
                break  
            else:
                print("Invalid input. Please enter y/Y/n/N.")
            
main()