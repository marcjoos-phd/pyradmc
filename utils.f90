module utils
  implicit none

contains
  
  subroutine compute_flux(image,nx,ny,flux)
    integer,intent(in)::nx,ny
    real(8),dimension(nx,ny),intent(in)::image
    real(8),intent(out)::flux
    integer::i,j

    flux = 0.

    do i = 1, nx
       do j = 1, ny
          flux = flux + image(i,j)
       enddo
    enddo

  end subroutine compute_flux

end module utils
