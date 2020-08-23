import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SculptorsComponent } from './sculptors.component';

describe('SculptorsComponent', () => {
  let component: SculptorsComponent;
  let fixture: ComponentFixture<SculptorsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SculptorsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SculptorsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
