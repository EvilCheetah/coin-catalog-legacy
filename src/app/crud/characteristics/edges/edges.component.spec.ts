import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EdgesComponent } from './edges.component';

describe('EdgesComponent', () => {
  let component: EdgesComponent;
  let fixture: ComponentFixture<EdgesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EdgesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EdgesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
