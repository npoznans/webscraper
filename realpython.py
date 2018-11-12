import new_webscrape as m

if __name__ == '__main__':
    print('Getting list of names.....')
    names = m.get_names()
    print('..... done.\n')

    results = []

    print('Getting stats for each name.....')

    for name in names:
        try:
            hits = m.get_hits_on_name(name)
            if hits is None:
                hits = -1
            results.append((hits, name))
        except:
            results.append((-1, name))
            m.log_error('error encountered while processing '
                      '{}, skipping'.format(name))
    print('.... done.\n')
    results.sort()
    results.reverse()

    if len(results) > 5:
        top_marks = results[:5]
    else:
        top_marks = results

    print('\nThe most popular mathematicians are, in descending order:\n')
    for (mark, m) in top_marks:
        print('{} with {} page views'.format(m, mark))

    no_results = len([res for res in results if res[0] == -1])
    print('\nBut we did not find results for '
          '{} mathematicians on the list'.format(no_results))
