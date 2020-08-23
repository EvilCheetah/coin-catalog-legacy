import { TestBed } from '@angular/core/testing';

import { SculptorsService } from './sculptors.service';

describe('SculptorsService', () => {
  let service: SculptorsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SculptorsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
