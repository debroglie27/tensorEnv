# Sample Input
Person1_List = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
Person1_NList = ['9:00', '20:00']

Person2_List = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
Person2_NList = ['10:00', '18:30']

Meet_Time = 30


def free_time_individual(person_list, person_not_list):
    person_freelist = []
    temp = 0

    for i in range(0, len(person_list) + 1):
        if i == 0:
            person_freelist.append([person_not_list[0], person_list[i][0]])
            temp = person_list[i][1]
        elif i == len(person_list):
            person_freelist.append([temp, person_not_list[1]])
        else:
            person_freelist.append([temp, person_list[i][0]])
            temp = person_list[i][1]

    return person_freelist


def convert(person_freelist, meet_time):
    person_converted_list = []

    for interval in person_freelist:
        temp1, temp2 = list(map(int, interval[0].split(':'))), list(map(int, interval[1].split(':')))
        temp1[0], temp2[0] = temp1[0] * 60, temp2[0] * 60
        temp = [sum(temp1), sum(temp2)]

        if abs(temp[0] - temp[1]) >= meet_time:
            person_converted_list.append(temp)

    return person_converted_list


def meeting_timings_non_formatted(p1_converted_list, p2_converted_list, meet_time):
    meeting_timings_list = []

    for interval1 in p1_converted_list:
        for interval2 in p2_converted_list:

            if not (interval1[0] > interval2[1] or interval1[1] < interval2[0]):
                temp = [max(interval1[0], interval2[0]), min(interval1[1], interval2[1])]
                if abs(temp[0] - temp[1]) >= meet_time:
                    meeting_timings_list.append(temp)

    return meeting_timings_list


def de_convert(meeting_timings_list):
    final_meeting_list = []

    for interval in meeting_timings_list:
        temp1, temp2, temp3, temp4 = interval[0] // 60, interval[0] % 60, interval[1] // 60, interval[1] % 60

        if temp2 == 0:
            temp2 = str(temp2) + '0'
        if temp4 == 0:
            temp4 = str(temp4) + '0'

        temp = [':'.join([str(temp1), str(temp2)]), ':'.join([str(temp3), str(temp4)])]
        final_meeting_list.append(temp)

    return final_meeting_list


def find_meeting_timings(person1_list, person1_not_list, person2_list, person2_not_list, meet_time):
    person1_freelist = free_time_individual(person1_list, person1_not_list)
    person2_freelist = free_time_individual(person2_list, person2_not_list)

    person1_converted_list = convert(person1_freelist, meet_time)
    person2_converted_list = convert(person2_freelist, meet_time)

    non_formatted_meeting_timings = meeting_timings_non_formatted(person1_converted_list, person2_converted_list, Meet_Time)

    final_meeting_timings = de_convert(non_formatted_meeting_timings)

    return final_meeting_timings


Final_Meetings_Timings = find_meeting_timings(Person1_List, Person1_NList, Person2_List, Person2_NList, Meet_Time)
print("\n", Final_Meetings_Timings)
