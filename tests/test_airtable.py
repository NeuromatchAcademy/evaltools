from pytest import fixture

from evaltools import airtable


@fixture
def form():
    return airtable.AirtableForm('NMA')


def test_add_event(form):
    form.add_event('test')
    assert len(form.events) == 2
    assert form.events[1]['event'] == 'test'


def test_add_answer(form):
    form.add_answer('test')
    assert len(form.answers) == 1
    assert form.answers[0] == 'test'
    assert len(form.events) == 2
    assert form.events[1]['event'] == 'answer'
