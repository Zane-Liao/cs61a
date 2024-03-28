test = {
  'name': 'no-repeats',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (no-repeats (list 5 4 2))
          7b50728ce8b33c4177f431bed9d19ca0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (no-repeats (list 5 4 5 4 2 2))
          7b50728ce8b33c4177f431bed9d19ca0
          # locked
          scm> (no-repeats (list 5 5 5 5 5))
          a269eabb0ee373aa84d82fff220ba9e5
          # locked
          scm> (no-repeats ())
          7b043779e02c43bdcd630251dbb3ebc9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (no-repeats '(5 4 3 2 1))
          (5 4 3 2 1)
          scm> (no-repeats '(5 4 3 2 1 1))
          (5 4 3 2 1)
          scm> (no-repeats '(5 5 4 3 2 1))
          (5 4 3 2 1)
          scm> (no-repeats '(12))
          (12)
          scm> (no-repeats '(1 1 1 1 1 1))
          (1)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
