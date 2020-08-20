import { TestBed } from '@angular/core/testing';

import { QualitiesService } from './qualities.service';

describe('QualitiesService', () => {
  let service: QualitiesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(QualitiesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
