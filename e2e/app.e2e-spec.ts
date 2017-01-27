import { ElevatorPage } from './app.po';

describe('elevator App', function() {
  let page: ElevatorPage;

  beforeEach(() => {
    page = new ElevatorPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
