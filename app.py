import streamlit as st
import streamlit.components.v1 as components


def paginator(label, items, items_per_page=10, on_sidebar=False):
    """Lets the user paginate a set of items.
    Parameters
    ----------
    label : str
        The label to display over the pagination widget.
    items : Iterator[Any]
        The items to display in the paginator.
    items_per_page: int
        The number of items to display per page.
    on_sidebar: bool
        Whether to display the paginator widget on the sidebar.

    Returns
    -------
    Iterator[Tuple[int, Any]]
        An iterator over *only the items on that page*, including
        the item's index.
    Example
    -------
    """

    # Figure out where to display the paginator
    if on_sidebar:
        location = st.sidebar.empty()
    else:
        location = st.empty()

    # Display a pagination selectbox in the specified location.
    items = list(items)
    n_pages = len(items)
    n_pages = (len(items) - 1) // items_per_page + 1
    page_format_func = lambda i: f"Mahageeta {n_pages*(i+1)-9} - {n_pages*(i+1)}"
    page_number = location.selectbox(
        label, range(n_pages), format_func=page_format_func
    )

    # Iterate over the items in the page to let the user display them.
    min_index = page_number * items_per_page
    max_index = min_index + items_per_page
    import itertools

    return itertools.islice(enumerate(items), min_index, max_index)


def paginate():
    title = [
        ("Maha Geeta 91.mp3", "1uivi0bvDrGqvIMmIqdFp9CxEgtLtIvKY"),
        ("Maha Geeta 90.mp3", "1DH9XRZrry1c2dU2LVHb9a76uaP91gv9J"),
        ("Maha Geeta 89.mp3", "14ovnzVBcm8YUcMCfny7EpvwP89pySuue"),
        ("Maha Geeta 88.mp3", "14SSGBORNg-WCmq2p6GhmZhv1-AtHhNFF"),
        ("Maha Geeta 87.mp3", "1uVCgavDxUlx7SDzUczZRbngC9_FUOQFt"),
        ("Maha Geeta 86.mp3", "12BDTp2SMhIDYsnulYQbUQ-YbV8qp1jCI"),
        ("Maha Geeta 85.mp3", "1syr0Mu-K6S4XYCudmPQQXIlrQw6rmepq"),
        ("Maha Geeta 84.mp3", "1A9_yAIJ83CX9t3ZzAJZ3ZGSMHPWec8zT"),
        ("Maha Geeta 83.mp3", "1M1U0X4KGYQTAKVeJX8aDZtwLYjrvknhf"),
        ("Maha Geeta 82.mp3", "1XlMZ_usfZfBCctdH1IDPYa9kAA9bAiQM"),
        ("Maha Geeta 81.mp3", "1coaFRZpwEVT18exXexI1niIWXm5D-6iU"),
        ("Maha Geeta 80.mp3", "1q3JQbmN7WdBnTEHrv1JYkh4mH5wWP1Rj"),
        ("Maha Geeta 79.mp3", "1-aUlhv1at8pskow7upUQwvZ5Tw9G4XDq"),
        ("Maha Geeta 78.mp3", "1CE319nkfUy-2_pbj9_s63YjWh8n-wEUY"),
        ("Maha Geeta 77.mp3", "1n8_DXwRH2IPA1K8TCsQPENIFrtYb7jWm"),
        ("Maha Geeta 76.mp3", "1HV_RHy0-vNBNfKZPCVw9iCrw5IL1h04W"),
        ("Maha Geeta 75.mp3", "1wPm9gdohK3mtVzcPqFq8Uypt3OhLcA7P"),
        ("Maha Geeta 74.mp3", "1pzXrrB4F587uWaAtFDghtsEqrH4ru2iX"),
        ("Maha Geeta 73.mp3", "1cL0jMKyRbd3Bud7MLP-Eu00ut0KzquDF"),
        ("Maha Geeta 72.mp3", "1L9aHdfQzwBKmFQLPe60_ZcJtO9YXi4au"),
        ("Maha Geeta 71.mp3", "1aBjj2wJh3Zv6FTVghNNCC_xrZQUAJ_OK"),
        ("Maha Geeta 70.mp3", "1IdGCQp8xVUuCIoRz1zXFj7QyK5GFpk9q"),
        ("Maha Geeta 69.mp3", "13JSLg_KbcLpO3EQF9GTc_gZA0EaQo97u"),
        ("Maha Geeta 68.mp3", "1OT95ppd8C2eDJyInj4oIpm4apZ6PspRL"),
        ("Maha Geeta 67.mp3", "11cbL4Gy-nDbezWM6Zg8LiMVVu9UmYUb3"),
        ("Maha Geeta 66.mp3", "15fzbnkhGOicBAyRPRbQlI_qNEzVk9BrH"),
        ("Maha Geeta 65.mp3", "1KQMcOvXuTlsAV4BFbxt2y5QPWyOfJAPS"),
        ("Maha Geeta 64.mp3", "1Ex8cwJPi1vzKtgFgwh5GiwGxLmVXtdUf"),
        ("Maha Geeta 63.mp3", "1P7gJ2JF8NhU5T91U-0Igo9BuZsAfBvOc"),
        ("Maha Geeta 62.mp3", "1kUD3JJG2LFHFvFPUnJfNqaFq0YMvdkuJ"),
        ("Maha Geeta 61.mp3", "1LwONUoRlRpO-PPF-PF7zqr41R7e1BqQs"),
        ("Maha Geeta 60.mp3", "1oYZrEfxZI7obAHSDtgpWr3DgPaSy2p6f"),
        ("Maha Geeta 59.mp3", "1-lDOfkqxevTNWsoIgSlnjLvi7Jojx6nO"),
        ("Maha Geeta 58.mp3", "1XNIMvhZGMb4jhhBZBmT3fxoRiuFSWliR"),
        ("Maha Geeta 57.mp3", "1DH3yR83sCYXDQV4tVvZEXNNCPUemAYJG"),
        ("Maha Geeta 56.mp3", "1aMr4161qvEcX_mgUk1PMJNEHVmWc4CIu"),
        ("Maha Geeta 55.mp3", "1ghUCa7WiTRis6xQ8ipoM-Cob_EULTcES"),
        ("Maha Geeta 54.mp3", "1HiiPmMpC1WudkTWDSduhsC6CQac9qjHJ"),
        ("Maha Geeta 53.mp3", "1kHv2cc7aJFEVoFZAOV6gNHgaRndNaYYt"),
        ("Maha Geeta 52.mp3", "1Xn6m_sUHROAndiTOgHmfIOEQc2kIHgac"),
        ("Maha Geeta 51.mp3", "1nweR4l0TPo6LqPSVobWZErePKmP0thjl"),
        ("Maha Geeta 50.mp3", "18PGuCtnVSo-_M9GZrEOFKK4f-N93kTh-"),
        ("Maha Geeta 49.mp3", "10UaFaoWjaO3x-gmy6gPCWcp8d_q_3ojl"),
        ("Maha Geeta 48.mp3", "1f8wDBHYUfJK0I9w0g0T8w4XJvcbzh8QW"),
        ("Maha Geeta 47.mp3", "1ui-Zggwb7glvZTErpHKgb4d2y4O6L9zz"),
        ("Maha Geeta 46.mp3", "1xTHqTzsnWxFBv_5garLyojEcItBRPqKz"),
        ("Maha Geeta 45.mp3", "1UlWP8JriCWAm8HQeZWEcweqnWZJGj91A"),
        ("Maha Geeta 44.mp3", "1LnUKMYzBrBbpaDf98ic_seJNeT5oaql4"),
        ("Maha Geeta 43.mp3", "1I81cSbTqlicnjeI_HBXZHs3Fb6-gtGnx"),
        ("Maha Geeta 42.mp3", "1mq0WDkN9Ql0MFsT42tfmGcY2HFCZc6Yc"),
        ("Maha Geeta 41.mp3", "13sX9BgVVpzphVirRKwXB1SmBLZn40yT9"),
        ("Maha Geeta 40.mp3", "1bYB-ugPF_UsON-K9lAowA0QyeUdCM3B6"),
        ("Maha Geeta 39.mp3", "1CixmPyeF-stgfEJrlmxp1LLh5o7y2j60"),
        ("Maha Geeta 38.mp3", "1WeGJY8IGN-J_fGu_vzRvF_RtBcDJC2kA"),
        ("Maha Geeta 37.mp3", "1QG59AxWirSTf9317O07AnWR3w-u8o8J1"),
        ("Maha Geeta 36.mp3", "1H3DPSzn2ou-6VZCW1uEFgZYFVgXlpu9r"),
        ("Maha Geeta 35.mp3", "1AMhwNfGzqKAQg4HzBK9t-hzkWixo1CP6"),
        ("Maha Geeta 34.mp3", "103v4KTWrCDbm0-IBq6bUk72CDuOloyDZ"),
        ("Maha Geeta 33.mp3", "12WitvittlDg6IR9e5MF2fiWW7UBCRsZV"),
        ("Maha Geeta 32.mp3", "18WVxobUB8CQKlFuAmtbY9zX0-b4dPPpM"),
        ("Maha Geeta 31.mp3", "1pPP91z29xLqqWQ0PCcgyfUlmnju9ltKi"),
        ("Maha Geeta 30.mp3", "1llRSPTPVbp0-CkTxN7abjb1ZnQw2JjXs"),
        ("Maha Geeta 29.mp3", "1B59TUq0tewqNpaORwHfe3iq5FdPr4OB1"),
        ("Maha Geeta 28.mp3", "1T5HOcPq4wU6Z50Nx6h7eNipxCyM6W3wh"),
        ("Maha Geeta 27.mp3", "1uCQMUVJsPUxFonLWaEHeGQdgfwZq0pH4"),
        ("Maha Geeta 26.mp3", "1YaTH5_x_kTemyLa8HMDunyWV6pFEoOTm"),
        ("Maha Geeta 25.mp3", "1h4qFhhZ7RUOZtbLkfKJH0PCf-VTfVDIc"),
        ("Maha Geeta 24.mp3", "18exA25Kp-dr1i0A3HW9JsySR9sF08ycU"),
        ("Maha Geeta 23.mp3", "1cIh0xcya3oz4g9KEoXlB2qVKonybfhHE"),
        ("Maha Geeta 22.mp3", "1w8KpFMkxkQtMXdtbi0_BLoCI98U_6sUn"),
        ("Maha Geeta 21.mp3", "1hvWu7OGCEBk1ikfVEynZJ_FXNrHugE8s"),
        ("Maha Geeta 20.mp3", "1cmlcwxHEL7zZ_bFDzRHkvdcNJS7-88na"),
        ("Maha Geeta 19.mp3", "1TiUJrZ4V7xE-4Cl7SCiGIYobIMTMQ4y-"),
        ("Maha Geeta 18.mp3", "1794Ngy9eSXfwgUP8uV4S1MbxNwQu-ihY"),
        ("Maha Geeta 17.mp3", "1OWRxRpJQHiUfObeo9wCR36bSCWloUaOz"),
        ("Maha Geeta 16.mp3", "193w2rKUgKwB26BW6s9pxy8GgkQyrnXI7"),
        ("Maha Geeta 15.mp3", "1WRNa2rbCJHC2f5q0IWYdXWUM0MmUtIaD"),
        ("Maha Geeta 14.mp3", "1Atbv6yd_pGP8_AlJF34t5YZjLYTt0cRa"),
        ("Maha Geeta 13.mp3", "1BcCR-T0UsXlJ3dtA8rpwXTFkWfC-6K_S"),
        ("Maha Geeta 12.mp3", "1HR0XhNJu4dlz1fgNvtkLWjDBCRTJ55wG"),
        ("Maha Geeta 11.mp3", "1vDNOxOe-h14-FdFJLuK9REZwGaHBrvje"),
        ("Maha Geeta 10.mp3", "1ezoYPbFHf5Q1lyIdCG9Iwx0p_CppfjfB"),
        ("Maha Geeta 09.mp3", "1KbukfQIRXIYeVXAtq9cIm2PTLmTrL5Fm"),
        ("Maha Geeta 08.mp3", "1iztQSxqtCQ22HAgXEmO_jnqPo34gYUI0"),
        ("Maha Geeta 07.mp3", "17nmpfAi_ndygUnMtGtP9wSSM9rXd8nXL"),
        ("Maha Geeta 06.mp3", "1lCma7qQMUqn3e3GnqzdJGA0eJ3RhiqyU"),
        ("Maha Geeta 05.mp3", "1dG5i7PRnazxdpREK0ApWTa_XR3iZSF5x"),
        ("Maha Geeta 04.mp3", "1cKaOEK4No5TNY4i8ix_h-UMWhaSUr0wk"),
        ("Maha Geeta 03.mp3", "1UQ08fK2DL3yrvnGLKhORPxTvt68xS1oI"),
        ("Maha Geeta 02.mp3", "18DUl4M8dTgWwB3x7NMHOw2mQU_yPSSLd"),
        ("Maha Geeta 01.mp3", "1DLSSVWz5KNPSoZUfrcrJaXwZ-igfsBWZ"),
    ]

    title.reverse()

    title_name = [i[0] for i in title]

    title_id = dict(title)

    for i, temp in paginator("Select a page", title_name):
        components.iframe(
            src=f"https://drive.google.com/file/d/{title_id[temp]}/preview",
            width=640,
            height=60,
        )
        st.text(temp)


if __name__ == "__main__":
    st.title("Astavakra Mahageeta")
    paginate()