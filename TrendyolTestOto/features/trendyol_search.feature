
Feature: Kullanıcı Trendyol'da ürün arar, filtre uygular ve sepete ekler

  Scenario: Kullanıcı Trendyol'da ürün arar
    Given kullanıcı Trendyol ana sayfasındadır
    When kullanıcı çerezleri kabul eder
    Then kullanıcı arama kutusuna "telefon" yazar ve arama yapar
    Then kullanıcı ilk ürünü seçer
    Then konum seç işaretlenir
    Then kullanıcı ürünü sepete ekler
    Then kullanıcı ana sayfaya döner

  Scenario: Kullanıcı "laptop" arar, filtre uygular ve ikinci ürünü sepete ekler
      Given kullanıcı ana sayfada arama kutusuna "laptop" yazar ve arama yapar
      When kullanıcı "hp" markasını filtreler
      Then kullanıcı ikinci ürünü seçer
      Then kullanıcı ikinci ürünü sepete ekler

  Scenario: Kullanıcı sepete gider ve kontrol eder
    Given kullanıcı sepete gider
    Then kullanıcı sepette en az 1 ürün olduğunu doğrular
